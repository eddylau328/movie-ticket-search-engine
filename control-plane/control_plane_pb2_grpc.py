# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import control_plane_pb2 as control__plane__pb2


class ControlPlaneStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getAvailableMovieList = channel.unary_unary(
                '/ControlPlane/getAvailableMovieList',
                request_serializer=control__plane__pb2.GetAvailableMovieListRequest.SerializeToString,
                response_deserializer=control__plane__pb2.GetAvailableMovieListResponse.FromString,
                )
        self.getMovieDetail = channel.unary_unary(
                '/ControlPlane/getMovieDetail',
                request_serializer=control__plane__pb2.GetMovieDetailsRequest.SerializeToString,
                response_deserializer=control__plane__pb2.MovieDetail.FromString,
                )
        self.getCinemaList = channel.unary_unary(
                '/ControlPlane/getCinemaList',
                request_serializer=control__plane__pb2.GetCinemaListRequest.SerializeToString,
                response_deserializer=control__plane__pb2.GetCinemaListResponse.FromString,
                )
        self.getMovieTimeslots = channel.unary_unary(
                '/ControlPlane/getMovieTimeslots',
                request_serializer=control__plane__pb2.GetMovieTimeslotsRequest.SerializeToString,
                response_deserializer=control__plane__pb2.GetMovieTimeslotsResponse.FromString,
                )


class ControlPlaneServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getAvailableMovieList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMovieDetail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getCinemaList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMovieTimeslots(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ControlPlaneServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getAvailableMovieList': grpc.unary_unary_rpc_method_handler(
                    servicer.getAvailableMovieList,
                    request_deserializer=control__plane__pb2.GetAvailableMovieListRequest.FromString,
                    response_serializer=control__plane__pb2.GetAvailableMovieListResponse.SerializeToString,
            ),
            'getMovieDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.getMovieDetail,
                    request_deserializer=control__plane__pb2.GetMovieDetailsRequest.FromString,
                    response_serializer=control__plane__pb2.MovieDetail.SerializeToString,
            ),
            'getCinemaList': grpc.unary_unary_rpc_method_handler(
                    servicer.getCinemaList,
                    request_deserializer=control__plane__pb2.GetCinemaListRequest.FromString,
                    response_serializer=control__plane__pb2.GetCinemaListResponse.SerializeToString,
            ),
            'getMovieTimeslots': grpc.unary_unary_rpc_method_handler(
                    servicer.getMovieTimeslots,
                    request_deserializer=control__plane__pb2.GetMovieTimeslotsRequest.FromString,
                    response_serializer=control__plane__pb2.GetMovieTimeslotsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ControlPlane', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ControlPlane(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getAvailableMovieList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlPlane/getAvailableMovieList',
            control__plane__pb2.GetAvailableMovieListRequest.SerializeToString,
            control__plane__pb2.GetAvailableMovieListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMovieDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlPlane/getMovieDetail',
            control__plane__pb2.GetMovieDetailsRequest.SerializeToString,
            control__plane__pb2.MovieDetail.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getCinemaList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlPlane/getCinemaList',
            control__plane__pb2.GetCinemaListRequest.SerializeToString,
            control__plane__pb2.GetCinemaListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMovieTimeslots(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ControlPlane/getMovieTimeslots',
            control__plane__pb2.GetMovieTimeslotsRequest.SerializeToString,
            control__plane__pb2.GetMovieTimeslotsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class EnquiryBotStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getAvailableMovieList = channel.unary_unary(
                '/EnquiryBot/getAvailableMovieList',
                request_serializer=control__plane__pb2.GetAvailableMovieListRequest.SerializeToString,
                response_deserializer=control__plane__pb2.GetAvailableMovieListResponse.FromString,
                )
        self.getMovieDetail = channel.unary_unary(
                '/EnquiryBot/getMovieDetail',
                request_serializer=control__plane__pb2.GetMovieDetailsRequest.SerializeToString,
                response_deserializer=control__plane__pb2.MovieDetail.FromString,
                )
        self.getCinemaList = channel.unary_unary(
                '/EnquiryBot/getCinemaList',
                request_serializer=control__plane__pb2.GetCinemaListRequest.SerializeToString,
                response_deserializer=control__plane__pb2.GetCinemaListResponse.FromString,
                )
        self.getMovieTimeslots = channel.unary_unary(
                '/EnquiryBot/getMovieTimeslots',
                request_serializer=control__plane__pb2.GetMovieTimeslotsRequest.SerializeToString,
                response_deserializer=control__plane__pb2.GetMovieTimeslotsResponse.FromString,
                )


class EnquiryBotServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getAvailableMovieList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMovieDetail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getCinemaList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMovieTimeslots(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EnquiryBotServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getAvailableMovieList': grpc.unary_unary_rpc_method_handler(
                    servicer.getAvailableMovieList,
                    request_deserializer=control__plane__pb2.GetAvailableMovieListRequest.FromString,
                    response_serializer=control__plane__pb2.GetAvailableMovieListResponse.SerializeToString,
            ),
            'getMovieDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.getMovieDetail,
                    request_deserializer=control__plane__pb2.GetMovieDetailsRequest.FromString,
                    response_serializer=control__plane__pb2.MovieDetail.SerializeToString,
            ),
            'getCinemaList': grpc.unary_unary_rpc_method_handler(
                    servicer.getCinemaList,
                    request_deserializer=control__plane__pb2.GetCinemaListRequest.FromString,
                    response_serializer=control__plane__pb2.GetCinemaListResponse.SerializeToString,
            ),
            'getMovieTimeslots': grpc.unary_unary_rpc_method_handler(
                    servicer.getMovieTimeslots,
                    request_deserializer=control__plane__pb2.GetMovieTimeslotsRequest.FromString,
                    response_serializer=control__plane__pb2.GetMovieTimeslotsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EnquiryBot', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EnquiryBot(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getAvailableMovieList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EnquiryBot/getAvailableMovieList',
            control__plane__pb2.GetAvailableMovieListRequest.SerializeToString,
            control__plane__pb2.GetAvailableMovieListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMovieDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EnquiryBot/getMovieDetail',
            control__plane__pb2.GetMovieDetailsRequest.SerializeToString,
            control__plane__pb2.MovieDetail.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getCinemaList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EnquiryBot/getCinemaList',
            control__plane__pb2.GetCinemaListRequest.SerializeToString,
            control__plane__pb2.GetCinemaListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMovieTimeslots(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EnquiryBot/getMovieTimeslots',
            control__plane__pb2.GetMovieTimeslotsRequest.SerializeToString,
            control__plane__pb2.GetMovieTimeslotsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
