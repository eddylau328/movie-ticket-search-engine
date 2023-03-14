from concurrent import futures
import sys
import argparse

from common import Provider
from server import EnquiryBotService
import enquiry_bot
import control_plane_pb2_grpc as pb2_grpc

import grpc


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'provider', type=str, help=f'An string for identifing which bot to instantiate')
    args = parser.parse_args()
    if args.provider not in [e.value for e in Provider]:
        # exit with error
        sys.exit(f'Invalid Provider {args.provider}')

    bot = None
    if args.provider == Provider.MCL:
        bot = enquiry_bot.MCLEnquiryBot()
    elif args.provider == Provider.GOLDEN_HARVEST:
        bot = enquiry_bot.GoldenHarvestEnquiryBot()

    if not bot:
        # exit with error
        sys.exit(f'Not support {args.provider}')

    service = EnquiryBotService(bot)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_EnquiryBotServicer_to_server(service, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


# if __name__ == '__main__':
#     import pprint
#     import argparse
#     import asyncio
#     parser = argparse.ArgumentParser()
#     parser.add_argument(
#         'movie', type=str, help=f'An string for identifing which bot to instantiate')
#     args = parser.parse_args()
#     bot = enquiry_bot.GoldenHarvestEnquiryBot()
#     results = asyncio.run(bot.getMovieTimeslots(movie_name=args.movie))
#     pprint.pprint(results)
