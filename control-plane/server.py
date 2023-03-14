from typing import List, Dict
import itertools
import asyncio

from common import (
    Provider,
    EnquiryBotInterface,
    Movie,
    MovieDetail,
    Cinema,
    MovieTimeslot
)
import control_plane_pb2_grpc as pb2_grpc
import control_plane_pb2 as pb2


class ControlPlaneService(pb2_grpc.ControlPlaneServicer):

    def __init__(self):
        self.bots: Dict[Provider, EnquiryBotInterface] = {}

    def add_bots(self, provider: Provider, bot: EnquiryBotInterface):
        self.bots[provider] = bot

    @property
    def provider_bots(self):
        return [self.bots[e] for e in Provider if e in self.bots]

    def getAvailableMovieList(
        self,
        request,
        context
    ) -> List[Movie]:
        groups = asyncio.gather(*[
            bot.getAvailableMovieList()
            for bot in self.provider_bots
        ])
        results = list(itertools.chain.from_iterable(asyncio.run(groups)))
        return pb2.GetAvailableMovieListResponse(results)

    def getMovieDetail(
        self,
        request,
        context
    ) -> MovieDetail:
        return pb2.MovieDetail()

    def getCinemaList(
        self,
        request,
        context
    ) -> List[Cinema]:
        groups = [
            bot.getCinemaList()
            for bot in self.provider_bots
        ]
        print(groups)
        results = list(itertools.chain.from_iterable(groups))
        return pb2.GetCinemaListResponse(results)

    def getMovieTimeslots(
        self,
        request,
        context
    ) -> List[MovieTimeslot]:
        groups = asyncio.gather(*[
            bot.getMovieTimeslots(request.movie_name)
            for bot in self.provider_bots
        ])
        results = list(itertools.chain.from_iterable(asyncio.run(groups)))
        return pb2.GetMovieTimeslotsResponse(results)
