import enquiry_bot
import asyncio


if __name__ == '__main__':
    f = enquiry_bot.MCLEnquiryBot()
    movies = asyncio.run(f.get_movie_list())
    import pprint
    pprint.pprint(movies)
