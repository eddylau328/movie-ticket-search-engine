from typing import List, Tuple
from string import Template
from datetime import datetime
import itertools
import json

from common import (
    EnquiryBot,
    Cinema,
    Movie,
    MovieTimeslot,
    Provider,
    District,
    Territory
)

import pytz
from bs4 import BeautifulSoup
from lxml import etree
import aiohttp
import asyncio


class GoldenHarvestEnquiryBot(EnquiryBot):

    async def get_movie_timeslots(self, movie_id: str, **kwargs) -> List[MovieTimeslot]:

        async def get_price(session, price_url) -> List[float]:
            price_list_xpath = '/html/body/div[2]/div/p/u'
            async with session.get(price_url) as resp:
                text = await resp.read()
                soup = BeautifulSoup(text.decode('utf-8'), 'html.parser')
                dom = etree.HTML(str(soup))
                raw_price_list = dom.xpath(price_list_xpath)
                datum = [json.loads(item.get('data-message'))
                         for item in raw_price_list]
                for data in datum:
                    if data['typeName'] == 'Adult':
                        return data['price']
                return 0

        async def get_available_dates(session, url) -> List[str]:
            time_select_xpath = '//*[@id="time-select"]'
            dates = []
            async with session.get(detail_url) as resp:
                text = await resp.read()
                soup = BeautifulSoup(text.decode('utf-8'), 'html.parser')
                dom = etree.HTML(str(soup))
                for option in dom.xpath(time_select_xpath)[0].getchildren():
                    dates.append(option.get('value'))
            return dates

        async def get_timeslots(session, date, url) -> Tuple[List[MovieTimeslot], List[str]]:
            price_base_template_url = Template(
                'https://www.goldenharvest.com//seatPlan/index?type=read&film_show_id=$film_show_id&from_type=web'
            )
            cinema_name_xpath_template = Template(
                '/html/body/div[$movie_count]/div/div[1]/h1'
            )
            cinema_id_xpath_template = Template(
                '/html/body/div[$movie_count]/div/div[2]/a'
            )
            house_xpath_template = Template(
                '/html/body/div[$movie_count]/div/div[2]/a[$timeslot_count]/div/h2'
            )
            timeslots = []
            price_urls = []
            async with session.get(url) as resp:
                text = await resp.read()
                soup = BeautifulSoup(text.decode('utf-8'), 'html.parser')
                dom = etree.HTML(str(soup))
                for movie_count in range(1, len(dom.xpath('/html/body/div')) + 1):
                    cinema_name = dom.xpath(
                        cinema_name_xpath_template.safe_substitute(
                            movie_count=movie_count,
                        ),
                    )[0].text
                    timeslot_anchors = dom.xpath(
                        cinema_id_xpath_template.safe_substitute(
                            movie_count=movie_count,
                        ),
                    )
                    if timeslot_anchors == 0:
                        continue
                    cinema_id = timeslot_anchors[0].get(
                        'href').split('cinema_id=')[1].split('&')[0]
                    for timeslot_count in range(1, len(timeslot_anchors) + 1):
                        anchor = timeslot_anchors[timeslot_count - 1]
                        house = dom.xpath(
                            house_xpath_template.safe_substitute(
                                movie_count=movie_count,
                                timeslot_count=timeslot_count,
                            )
                        )[0].text
                        hk_zone = pytz.timezone('Asia/Hong_Kong')
                        # yyyy MM-DD
                        time = anchor.get('data-time')
                        start = datetime.strptime(
                            f'{date} {time}',
                            '%Y-%m-%d %H:%M',
                        ).astimezone(hk_zone)
                        timeslots.append(MovieTimeslot(
                            start=start,
                            price=0.0,
                            cinema_id=cinema_id,
                            cinema_name=cinema_name,
                            provider=self.provider,
                            house=house,
                        ))
                        price_urls.append(price_base_template_url.safe_substitute(
                            film_show_id=anchor.get('href').split(
                                'film_show_id=')[1].split('&')[0],
                        ))

            return timeslots, price_urls

        # date yyyy-mm-dd
        detail_page_url_template = Template(
            'https://www.goldenharvest.com/film/detail?film_id=$movie_id'
        )
        timeslot_query_url_template = Template(
            'https://www.goldenharvest.com//film/ajaxFilmShow?film_id=$movie_id&date=$date'
        )
        async with aiohttp.ClientSession() as session:
            detail_url = detail_page_url_template.safe_substitute(
                movie_id=movie_id)
            dates = await get_available_dates(session, detail_url)

            results = await asyncio.gather(*[
                get_timeslots(
                    session,
                    date,
                    timeslot_query_url_template.safe_substitute(
                        movie_id=movie_id,
                        date=date,
                    ),
                ) for date in dates
            ])
            timeslots = list(itertools.chain.from_iterable(
                [r[0] for r in results]))
            price_urls = list(itertools.chain.from_iterable(
                [r[1] for r in results]))
            prices = await asyncio.gather(*[get_price(session, price_url) for price_url in price_urls])
            for i, price in enumerate(prices):
                timeslots[i].price = price
            return timeslots

    async def get_available_movie_list(self, **kwargs) -> List[Movie]:
        template_url = Template(
            'https://www.goldenharvest.com//film/ajaxList?category=now&page=$page&lang=zh_tw'
        )
        id_anchor_xpath_template = Template(
            '/html/body/div[$index]/div/div[1]/a'
        )
        movie_name_xpath_template = Template(
            '/html/body/div[$index]/div/div[2]/div[1]'
        )
        results = []
        page = 0
        async with aiohttp.ClientSession() as session:
            while page <= 20:
                page += 1
                url = template_url.safe_substitute(page=page)
                async with session.get(url) as resp:
                    text = await resp.read()
                    if text == b'':
                        break
                    soup = BeautifulSoup(text.decode('utf-8'), 'html.parser')
                    dom = etree.HTML(str(soup))
                    for i in range(1, len(dom.xpath('/html/body')[0].getchildren())+1):
                        # <a href="/film/detail?film_id=2201" class="movie-detail-btn" />
                        id_anchor_xpath = id_anchor_xpath_template.safe_substitute(
                            index=i,
                        )
                        id = ''
                        for ch in dom.xpath(id_anchor_xpath)[0].get('href').split('film_id=')[1]:
                            if not ch.isnumeric():
                                break
                            id += ch
                        movie_name_xpath = movie_name_xpath_template.safe_substitute(
                            index=i,
                        )
                        movie_name = dom.xpath(movie_name_xpath)[0].text
                        results.append(Movie(id, movie_name))
        return results

    async def get_cinema_list(self) -> List[Cinema]:
        url = 'https://www.goldenharvest.com/film/list?category=now'
        detail_url_template = Template(
            'https://www.goldenharvest.com/cinema/schedule?cinema_id=$cinema_id',
        )
        cinema_menu_xpath = '/html/body/header/div[3]/div[3]/ul/li[5]/ul'
        cinema_ids = []

        async def get_detail_cinema(session, id, detail_url) -> Cinema:
            # the sky
            if id == '1':
                detail_url = 'https://www.theskycinema.com/cinema/map/cinema_id/1'
                async with session.get(detail_url) as resp:
                    text = await resp.read()
                    soup = BeautifulSoup(text.decode('utf-8'), 'html.parser')
                    dom = etree.HTML(str(soup))
                    cinema_name_xpath = '/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/h1'
                    address_xpath = '/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/p[1]/span'
                    cinema_name = dom.xpath(cinema_name_xpath)[0].text
                    address = dom.xpath(address_xpath)[0].text
            else:
                async with session.get(detail_url) as resp:
                    text = await resp.read()
                    soup = BeautifulSoup(text.decode('utf-8'), 'html.parser')
                    dom = etree.HTML(str(soup))
                    cinema_name_xpath = '/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/h1'
                    address_xpath = '/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/p[1]/span'
                    cinema_name = dom.xpath(cinema_name_xpath)[0].text
                    address = dom.xpath(address_xpath)[0].text
            return Cinema(
                id=id,
                name=cinema_name,
                address=address,
                provider=self.provider,
                district=District.map_address(address),
                territory=Territory.map_address(address),
            )

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                text = await resp.read()
                soup = BeautifulSoup(text.decode('utf-8'), 'html.parser')
                dom = etree.HTML(str(soup))
                menu = dom.xpath(cinema_menu_xpath)[0]
                for li in menu.getchildren():
                    anchor = li.getchildren()[0]
                    cinema_id = anchor.get('href').split('cinema_id=')[1]
                    cinema_ids.append(cinema_id)
            cinemas = await asyncio.gather(*[
                get_detail_cinema(
                    session,
                    id,
                    detail_url_template.safe_substitute(cinema_id=id),
                ) for id in cinema_ids]
            )
            return cinemas

    @ property
    def provider(self) -> Provider:
        return Provider.GOLDEN_HARVEST
