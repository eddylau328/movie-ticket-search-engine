from common import (
    Movie,
    MovieFetcher,
    Provider,
)
from typing import List

import aiohttp


class MCLFetcher(MovieFetcher):

    async def get_available_movie_list(self) -> List[Movie]:
        async with aiohttp.ClientSession() as session:
            url = 'https://www.mclcinema.com/MCLWebAPI2/GetNCF.aspx?l=1'
            async with session.get(url) as resp:
                result = await resp.json(content_type='text/html')
                return [
                    Movie(
                        id=str(m['id']),
                        name=m['mn'],
                        provider=self.provider.value,
                    ) for m in result.get('n', {}).get('n', [])
                ]

    @property
    def provider(self) -> Provider:
        return Provider.MCL
