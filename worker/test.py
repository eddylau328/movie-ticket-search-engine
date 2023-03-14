import control_plane_pb2_grpc as pb2_grpc
import control_plane_pb2 as pb2

import grpc


class EnquiryClient:
    def __init__(self):
        self.host = 'localhost'
        self.port = 50051
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.port))

        # bind the client and the server
        self.stub = pb2_grpc.EnquiryBotStub(self.channel)

    def getAvailableMovieList(self, **kwargs):
        """
        Client function to call the rpc for getAvailableMovieList
        """
        request_body = pb2.GetAvailableMovieListRequest(**kwargs)
        return self.stub.getAvailableMovieList(request_body)

    def getMovieDetail(self, id: str):
        """
        Client function to call the rpc for getMovieDetail
        """
        request_body = pb2.GetMovieDetailsRequest(id)
        return self.stub.getAvailableMovieList(request_body)

    def getCinemaList(self):
        """
        Client function to call the rpc for getCinemaList
        """
        request = pb2.GetCinemaListRequest()
        return self.stub.getCinemaList(request)

    def getMovieTimeslots(self, **kwargs):
        """
        Client function to call the rpc for getMovieTimeslots
        """
        request_body = pb2.GetMovieTimeslotsRequest(**kwargs)
        return self.stub.getMovieTimeslots(request_body)


if __name__ == '__main__':
    client = EnquiryClient()
    # result = client.getCinemaList()
    # print(result)
    result = client.getMovieTimeslots(movie_name='鈴芽之旅')
    print(result)
