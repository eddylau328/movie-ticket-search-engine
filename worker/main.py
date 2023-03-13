import enquiry_bot
import asyncio


if __name__ == '__main__':
    f = enquiry_bot.MCLEnquiryBot()
    movies = asyncio.run(f.get_available_movie_list())
    cinemas = asyncio.run(f.get_cinema_list())
    timeslots = asyncio.run(f.get_movie_timeslots(
        movie_id=movies[0].id,
    ))
    import pprint
    # pprint.pprint(movies)
    # pprint.pprint(cinemas)
    pprint.pprint(timeslots)
