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
        results = list(itertools.chain.from_iterable(groups))
        return pb2.GetCinemaListResponse(
            cinema_list=results,
        )

    def getMovieTimeslots(
        self,
        request,
        context
    ) -> List[MovieTimeslot]:
        results = []
        for bot in self.provider_bots:
            response = bot.getMovieTimeslots(
                movie_name=request.movie_name
            )
            results += response.movie_timeslots
        results = [
            pb2.MovieTimeslot(
                start=timeslot.start,
                price=timeslot.price,
                house=timeslot.house,
                cinema_id=timeslot.cinema_id,
                cinema_name=timeslot.cinema_name,
            ) for timeslot in results
        ]
        print(results[0])
        return pb2.GetMovieTimeslotsResponse(
            movie_timeslots=results,
        )
