from typing import List
from string import Template
from datetime import datetime

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
        return []

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
        # for option in dom.xpath(select_x_path)[0].getchildren():
        #     content = etree.fromstring(option.get('data-content'))
        #     # e.g. ['03月14日 (二)', '10:10 AM', 'IMAX / 7 院']
        #     chunks = content.xpath('/div/h1')[0].text.split(',')
        #     raw_date = chunks[0].split(' ')[0].replace(
        #         '月', '-').replace('日', '')
        #     raw_time = chunks[1]
        #     hk_zone = pytz.timezone('Asia/Hong_Kong')
        #     now = datetime.now(hk_zone)
        #     print(type(now.year))
        #     print(type(raw_date))
        #     print(type(raw_time))
        #     start = datetime.strftime(
        #         f'{now.year} {raw_date} {raw_time}',
        #         '%Y %m-%d %I:%M %p',
        #     )
        #     print(start)

        # MovieTimeslot(
        # dom.xpath('/html/body/div[1]/div/div[2]/div[1]')[0].text,
        # )

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
            # cinema = await get_detail_cinema(session, cinema_ids[0], detail_url_template.safe_substitute(cinema_id=cinema_ids[0]), )
            # cinemas = [cinema]
            return cinemas

    @ property
    def provider(self) -> Provider:
        return Provider.GOLDEN_HARVEST
