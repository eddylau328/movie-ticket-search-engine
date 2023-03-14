from concurrent import futures

from server import ControlPlaneService
from common import Provider
import control_plane_pb2_grpc as pb2_grpc

import grpc


def serve():
    service = ControlPlaneService()
    # service.add_bots(Provider.MCL, )
    # service.add_bots(Provider.GOLDEN_HARVEST, )
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ControlPlaneServicer_to_server(service, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
