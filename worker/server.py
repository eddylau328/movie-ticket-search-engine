from typing import List

import control_plane_pb2_grpc as pb2_grpc
import control_plane_pb2 as pb2
from common import (
    EnquiryBotInterface,
    Movie,
    MovieDetail,
    MovieTimeslot,
    Cinema,
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
        results = asyncio.run(self.bot.getCinemaList())
        return pb2.GetCinemaListResponse(results)

    def getMovieTimeslots(
        self,
        request,
        context,
    ) -> List[MovieTimeslot]:
        results = asyncio.run(self.bot.getMovieTimeslots(request.movie_name))
        return pb2.GetMovieTimeslotsResponse(results)
