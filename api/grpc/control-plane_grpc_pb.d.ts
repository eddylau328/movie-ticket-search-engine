// GENERATED CODE -- DO NOT EDIT!

// package:
// file: control-plane.proto

import * as control_plane_pb from "./control-plane_pb";
import * as grpc from "@grpc/grpc-js";

interface IControlPlaneService
  extends grpc.ServiceDefinition<grpc.UntypedServiceImplementation> {
  getAvailableMovieList: grpc.MethodDefinition<
    control_plane_pb.GetAvailableMovieListRequest,
    control_plane_pb.GetAvailableMovieListResponse
  >;
  getMovieDetail: grpc.MethodDefinition<
    control_plane_pb.GetMovieDetailsRequest,
    control_plane_pb.MovieDetail
  >;
  getCinemaList: grpc.MethodDefinition<
    control_plane_pb.GetCinemaListRequest,
    control_plane_pb.GetCinemaListResponse
  >;
  getMovieTimeslots: grpc.MethodDefinition<
    control_plane_pb.GetMovieTimeslotsRequest,
    control_plane_pb.GetMovieTimeslotsResponse
  >;
}

export const ControlPlaneService: IControlPlaneService;

export interface IControlPlaneServer extends grpc.UntypedServiceImplementation {
  getAvailableMovieList: grpc.handleUnaryCall<
    control_plane_pb.GetAvailableMovieListRequest,
    control_plane_pb.GetAvailableMovieListResponse
  >;
  getMovieDetail: grpc.handleUnaryCall<
    control_plane_pb.GetMovieDetailsRequest,
    control_plane_pb.MovieDetail
  >;
  getCinemaList: grpc.handleUnaryCall<
    control_plane_pb.GetCinemaListRequest,
    control_plane_pb.GetCinemaListResponse
  >;
  getMovieTimeslots: grpc.handleUnaryCall<
    control_plane_pb.GetMovieTimeslotsRequest,
    control_plane_pb.GetMovieTimeslotsResponse
  >;
}

export class ControlPlaneClient extends grpc.Client {
  constructor(
    address: string,
    credentials: grpc.ChannelCredentials,
    options?: object
  );
  getAvailableMovieList(
    argument: control_plane_pb.GetAvailableMovieListRequest,
    callback: grpc.requestCallback<control_plane_pb.GetAvailableMovieListResponse>
  ): grpc.ClientUnaryCall;
  getAvailableMovieList(
    argument: control_plane_pb.GetAvailableMovieListRequest,
    metadataOrOptions: grpc.Metadata | grpc.CallOptions | null,
    callback: grpc.requestCallback<control_plane_pb.GetAvailableMovieListResponse>
  ): grpc.ClientUnaryCall;
  getAvailableMovieList(
    argument: control_plane_pb.GetAvailableMovieListRequest,
    metadata: grpc.Metadata | null,
    options: grpc.CallOptions | null,
    callback: grpc.requestCallback<control_plane_pb.GetAvailableMovieListResponse>
  ): grpc.ClientUnaryCall;
  getMovieDetail(
    argument: control_plane_pb.GetMovieDetailsRequest,
    callback: grpc.requestCallback<control_plane_pb.MovieDetail>
  ): grpc.ClientUnaryCall;
  getMovieDetail(
    argument: control_plane_pb.GetMovieDetailsRequest,
    metadataOrOptions: grpc.Metadata | grpc.CallOptions | null,
    callback: grpc.requestCallback<control_plane_pb.MovieDetail>
  ): grpc.ClientUnaryCall;
  getMovieDetail(
    argument: control_plane_pb.GetMovieDetailsRequest,
    metadata: grpc.Metadata | null,
    options: grpc.CallOptions | null,
    callback: grpc.requestCallback<control_plane_pb.MovieDetail>
  ): grpc.ClientUnaryCall;
  getCinemaList(
    argument: control_plane_pb.GetCinemaListRequest,
    callback: grpc.requestCallback<control_plane_pb.GetCinemaListResponse>
  ): grpc.ClientUnaryCall;
  getCinemaList(
    argument: control_plane_pb.GetCinemaListRequest,
    metadataOrOptions: grpc.Metadata | grpc.CallOptions | null,
    callback: grpc.requestCallback<control_plane_pb.GetCinemaListResponse>
  ): grpc.ClientUnaryCall;
  getCinemaList(
    argument: control_plane_pb.GetCinemaListRequest,
    metadata: grpc.Metadata | null,
    options: grpc.CallOptions | null,
    callback: grpc.requestCallback<control_plane_pb.GetCinemaListResponse>
  ): grpc.ClientUnaryCall;
  getMovieTimeslots(
    argument: control_plane_pb.GetMovieTimeslotsRequest,
    callback: grpc.requestCallback<control_plane_pb.GetMovieTimeslotsResponse>
  ): grpc.ClientUnaryCall;
  getMovieTimeslots(
    argument: control_plane_pb.GetMovieTimeslotsRequest,
    metadataOrOptions: grpc.Metadata | grpc.CallOptions | null,
    callback: grpc.requestCallback<control_plane_pb.GetMovieTimeslotsResponse>
  ): grpc.ClientUnaryCall;
  getMovieTimeslots(
    argument: control_plane_pb.GetMovieTimeslotsRequest,
    metadata: grpc.Metadata | null,
    options: grpc.CallOptions | null,
    callback: grpc.requestCallback<control_plane_pb.GetMovieTimeslotsResponse>
  ): grpc.ClientUnaryCall;
}
