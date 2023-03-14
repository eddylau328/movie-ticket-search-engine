from concurrent import futures
import os

from server import ControlPlaneService
from worker_client import EnquiryBotClient
from common import Provider
import control_plane_pb2_grpc as pb2_grpc

import grpc


def serve():
    # Get environment variables
    mcl_url = os.getenv('MCL_BOT')
    golden_harvest_url = os.environ.get('GOLDEN_HARVEST_BOT')

    # setup service
    service = ControlPlaneService()
    service.add_bots(Provider.MCL, EnquiryBotClient(mcl_url))
    service.add_bots(Provider.GOLDEN_HARVEST,
                     EnquiryBotClient(golden_harvest_url))

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ControlPlaneServicer_to_server(service, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
