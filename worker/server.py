from typing import List

import control_plane_pb2_grpc as pb2_grpc
import control_plane_pb2 as pb2
from common import (
    EnquiryBotInterface,
    Movie,
    MovieDetail,
    MovieTimeslot,
    Cinema,
    Provider,
    Territory,
    District,
)

import asyncio


class EnquiryBotService(pb2_grpc.EnquiryBotServicer):

    def __init__(self, bot: EnquiryBotInterface):
        self.bot = bot

    def getAvailableMovieList(
        self,
        request,
        context,
    ) -> List[Movie]:
        results = asyncio.run(self.bot.getAvailableMovieList())
        return pb2.GetAvailableMovieListResponse(results)

    def getMovieDetail(
        self,
        request,
        context,
    ) -> MovieDetail:
        results = asyncio.run(self.bot.getMovieDetails(request.id))
        return pb2.MovieDetail()

    def getCinemaList(
        self,
        request,
        context,
    ) -> List[Cinema]:
        cinemas = asyncio.run(self.bot.getCinemaList())
        results = [
            pb2.Cinema(
                id=cinema.id,
                name=cinema.name,
                provider=Provider.map_proto_enum(cinema.provider),
                address=cinema.address,
                territory=Territory.map_proto_enum(cinema.territory),
                district=District.map_proto_enum(cinema.district),
            ) for cinema in cinemas
        ]
        return pb2.GetCinemaListResponse(
            cinema_list=results,
        )

    def getMovieTimeslots(
        self,
        request,
        context,
    ) -> List[MovieTimeslot]:
        print(request.movie_name)
        timeslots = asyncio.run(self.bot.getMovieTimeslots(request.movie_name))
        print(timeslots)
        results = [timeslot.proto() for timeslot in timeslots]
        return pb2.GetMovieTimeslotsResponse(
            movie_timeslots=results
        )
