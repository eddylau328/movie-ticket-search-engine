import grpc
import control_plane_pb2_grpc as pb2_grpc
import control_plane_pb2 as pb2


class EnquiryBotClient:
    """
    Enquiry Bot Client for gRPC functionality
    """

    # e.g. server_url 'localhost:50051'
    def __init__(self, server_url):
        self.channel = grpc.insecure_channel(server_url)
        # bind the client and the server
        self.stub = pb2_grpc.EnquiryBotStub(self.channel)

    async def getAvailableMovieList(self, **kwargs):
        """
        Client function to call the rpc for getAvailableMovieList
        """
        request_body = pb2.GetAvailableMovieListRequest(**kwargs)
        return self.stub.getAvailableMovieList(request_body)

    async def getMovieDetail(self, id: str):
        """
        Client function to call the rpc for getMovieDetail
        """
        request_body = pb2.GetMovieDetailsRequest(id)
        return self.stub.getAvailableMovieList(request_body)

    async def getCinemaList(self):
        """
        Client function to call the rpc for getCinemaList
        """
        request_body = pb2.GetCinemaListRequest()
        return self.stub.getCinemaList(request_body)

    async def getMovieTimeslots(self, **kwargs):
        """
        Client function to call the rpc for getMovieTimeslots
        """
        request_body = pb2.GetMovieTimeslotsRequest(**kwargs)
        return self.stub.getCinemaList(request_body)
