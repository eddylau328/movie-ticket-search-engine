from typing import List
from concurrent import futures
from common import (
    Movie,
    MovieDetail,
    MovieTimeslot,
    Cinema,
)

import grpc
import control_plane_pb2_grpc as pb2_grpc
import control_plane_pb2 as pb2


class ControlPlaneService(pb2_grpc.ControlPlaneServicer):
    def getAvailableMovieList(
        self,
        request,
        context
    ) -> List[Movie]:
        return pb2.GetAvailableMovieListResponse()

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
        return pb2.GetCinemaListResponse()

    def getMovieTimeslots(
        self,
        request,
        context
    ) -> List[MovieTimeslot]:
        return pb2.GetMovieTimeslotsResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ControlPlaneServicer_to_server(ControlPlaneService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
