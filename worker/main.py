import fetchers
import asyncio


if __name__ == '__main__':
    f = fetchers.MCLFetcher()
    movies = asyncio.run(f.get_movie_list())
    import pprint
    pprint.pprint(movies)
