from typing import List
from datetime import datetime
from string import Template
import itertools

from common import (
    Cinema,
    District,
    Territory,
    EnquiryBot,
    Provider,
    Movie,
    MovieTimeslot,
)

import aiohttp
import pytz
import asyncio


class MCLEnquiryBot(EnquiryBot):

    async def getAvailableMovieList(self) -> List[Movie]:
        async with aiohttp.ClientSession() as session:
            url = 'https://www.mclcinema.com/MCLWebAPI2/GetNCF.aspx?l=1'
            async with session.get(url) as resp:
                result = await resp.json(content_type='text/html')
                return [
                    Movie(
                        id=str(m['id']),
                        name=m['mn'],
                    ) for m in result.get('n', {}).get('n', [])
                ]

    async def getCinemaList(self) -> List[Cinema]:
        async with aiohttp.ClientSession() as session:
            url = 'https://www.mclcinema.com/MCLWebAPI2/GetCinemaDetails.aspx?l=1'
            async with session.get(url) as resp:
                result = await resp.json(content_type='text/html')
                return [
                    Cinema(
                        id=c['id'],
                        name=c['n'],
                        address=c['a'],
                        district=District.map_address(c['a']),
                        territory=Territory.map_address(c['a']),
                        provider=self.provider,
                    )
                    for c in result
                ]

    async def getMovieTimeslots(
        self,
        movie_name: str,
        **kwargs,
    ) -> List[MovieTimeslot]:
        movie_list = await self.getAvailableMovieList()
        movies = []
        for movie in movie_list:
            if movie_name in movie.name:
                movies.append(movie)
        if len(movies) == 0:
            return []

        async def get_individual(session, movie: Movie):
            template_url = Template(
                'https://www.mclcinema.com/MCLWebAPI2/GetShowDays.aspx?l=1&t=s&id=$movie_id'
            )
            url = template_url.safe_substitute(movie_id=movie.id)
            timeslots = []
            async with session.get(url) as resp:
                result = await resp.json(content_type='text/html')
                for item in result[0].get('sd', []):
                    raw_date = item['n']
                    for cinema_collection in item.get('c', []):
                        cinema_id = cinema_collection['ci']
                        cinema_name = cinema_collection['cn']
                        for raw_timeslot in cinema_collection.get('s', []):
                            chunk = raw_timeslot['sn'].split(', ')
                            hk_zone = pytz.timezone('Asia/Hong_Kong')
                            now = datetime.now(hk_zone)
                            time, time_locale = chunk[2].split(' ')
                            if int(time.split(':')[0]) > 12:
                                hour, minute = time.split(':')
                                time = f'{str(int(hour) - 12).zfill(2)}:{minute}'
                            start = datetime.strptime(
                                f'{now.year} {raw_date} {time} {time_locale}',
                                '%Y %d/%m %I:%M %p',
                            ).astimezone(hk_zone)
                            house, price = chunk[3].split('$')
                            timeslots.append(
                                MovieTimeslot(
                                    start=start,
                                    price=float(price.strip()),
                                    cinema_id=cinema_id,
                                    cinema_name=cinema_name,
                                    house=house.strip(),
                                    provider=self.provider,
                                    movie_name=movie.name,
                                )
                            )
                return timeslots

        async with aiohttp.ClientSession() as session:
            results = await asyncio.gather(*[get_individual(session, movie) for movie in movies])
        return list(itertools.chain.from_iterable(results))

    @property
    def provider(self) -> Provider:
        return Provider.MCL
