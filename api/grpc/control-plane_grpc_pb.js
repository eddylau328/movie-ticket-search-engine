// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('@grpc/grpc-js');
var control$plane_pb = require('./control-plane_pb.js');

function serialize_GetAvailableMovieListRequest(arg) {
  if (!(arg instanceof control$plane_pb.GetAvailableMovieListRequest)) {
    throw new Error('Expected argument of type GetAvailableMovieListRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_GetAvailableMovieListRequest(buffer_arg) {
  return control$plane_pb.GetAvailableMovieListRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_GetAvailableMovieListResponse(arg) {
  if (!(arg instanceof control$plane_pb.GetAvailableMovieListResponse)) {
    throw new Error('Expected argument of type GetAvailableMovieListResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_GetAvailableMovieListResponse(buffer_arg) {
  return control$plane_pb.GetAvailableMovieListResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_GetCinemaListRequest(arg) {
  if (!(arg instanceof control$plane_pb.GetCinemaListRequest)) {
    throw new Error('Expected argument of type GetCinemaListRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_GetCinemaListRequest(buffer_arg) {
  return control$plane_pb.GetCinemaListRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_GetCinemaListResponse(arg) {
  if (!(arg instanceof control$plane_pb.GetCinemaListResponse)) {
    throw new Error('Expected argument of type GetCinemaListResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_GetCinemaListResponse(buffer_arg) {
  return control$plane_pb.GetCinemaListResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_GetMovieDetailsRequest(arg) {
  if (!(arg instanceof control$plane_pb.GetMovieDetailsRequest)) {
    throw new Error('Expected argument of type GetMovieDetailsRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_GetMovieDetailsRequest(buffer_arg) {
  return control$plane_pb.GetMovieDetailsRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_GetMovieTimeslotsRequest(arg) {
  if (!(arg instanceof control$plane_pb.GetMovieTimeslotsRequest)) {
    throw new Error('Expected argument of type GetMovieTimeslotsRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_GetMovieTimeslotsRequest(buffer_arg) {
  return control$plane_pb.GetMovieTimeslotsRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_GetMovieTimeslotsResponse(arg) {
  if (!(arg instanceof control$plane_pb.GetMovieTimeslotsResponse)) {
    throw new Error('Expected argument of type GetMovieTimeslotsResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_GetMovieTimeslotsResponse(buffer_arg) {
  return control$plane_pb.GetMovieTimeslotsResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_MovieDetail(arg) {
  if (!(arg instanceof control$plane_pb.MovieDetail)) {
    throw new Error('Expected argument of type MovieDetail');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_MovieDetail(buffer_arg) {
  return control$plane_pb.MovieDetail.deserializeBinary(new Uint8Array(buffer_arg));
}


var ControlPlaneService = exports.ControlPlaneService = {
  getAvailableMovieList: {
    path: '/ControlPlane/getAvailableMovieList',
    requestStream: false,
    responseStream: false,
    requestType: control$plane_pb.GetAvailableMovieListRequest,
    responseType: control$plane_pb.GetAvailableMovieListResponse,
    requestSerialize: serialize_GetAvailableMovieListRequest,
    requestDeserialize: deserialize_GetAvailableMovieListRequest,
    responseSerialize: serialize_GetAvailableMovieListResponse,
    responseDeserialize: deserialize_GetAvailableMovieListResponse,
  },
  getMovieDetail: {
    path: '/ControlPlane/getMovieDetail',
    requestStream: false,
    responseStream: false,
    requestType: control$plane_pb.GetMovieDetailsRequest,
    responseType: control$plane_pb.MovieDetail,
    requestSerialize: serialize_GetMovieDetailsRequest,
    requestDeserialize: deserialize_GetMovieDetailsRequest,
    responseSerialize: serialize_MovieDetail,
    responseDeserialize: deserialize_MovieDetail,
  },
  getCinemaList: {
    path: '/ControlPlane/getCinemaList',
    requestStream: false,
    responseStream: false,
    requestType: control$plane_pb.GetCinemaListRequest,
    responseType: control$plane_pb.GetCinemaListResponse,
    requestSerialize: serialize_GetCinemaListRequest,
    requestDeserialize: deserialize_GetCinemaListRequest,
    responseSerialize: serialize_GetCinemaListResponse,
    responseDeserialize: deserialize_GetCinemaListResponse,
  },
  getMovieTimeslots: {
    path: '/ControlPlane/getMovieTimeslots',
    requestStream: false,
    responseStream: false,
    requestType: control$plane_pb.GetMovieTimeslotsRequest,
    responseType: control$plane_pb.GetMovieTimeslotsResponse,
    requestSerialize: serialize_GetMovieTimeslotsRequest,
    requestDeserialize: deserialize_GetMovieTimeslotsRequest,
    responseSerialize: serialize_GetMovieTimeslotsResponse,
    responseDeserialize: deserialize_GetMovieTimeslotsResponse,
  },
};

exports.ControlPlaneClient = grpc.makeGenericClientConstructor(ControlPlaneService);
var EnquiryBotService = exports.EnquiryBotService = {
  getAvailableMovieList: {
    path: '/EnquiryBot/getAvailableMovieList',
    requestStream: false,
    responseStream: false,
    requestType: control$plane_pb.GetAvailableMovieListRequest,
    responseType: control$plane_pb.GetAvailableMovieListResponse,
    requestSerialize: serialize_GetAvailableMovieListRequest,
    requestDeserialize: deserialize_GetAvailableMovieListRequest,
    responseSerialize: serialize_GetAvailableMovieListResponse,
    responseDeserialize: deserialize_GetAvailableMovieListResponse,
  },
  getMovieDetail: {
    path: '/EnquiryBot/getMovieDetail',
    requestStream: false,
    responseStream: false,
    requestType: control$plane_pb.GetMovieDetailsRequest,
    responseType: control$plane_pb.MovieDetail,
    requestSerialize: serialize_GetMovieDetailsRequest,
    requestDeserialize: deserialize_GetMovieDetailsRequest,
    responseSerialize: serialize_MovieDetail,
    responseDeserialize: deserialize_MovieDetail,
  },
  getCinemaList: {
    path: '/EnquiryBot/getCinemaList',
    requestStream: false,
    responseStream: false,
    requestType: control$plane_pb.GetCinemaListRequest,
    responseType: control$plane_pb.GetCinemaListResponse,
    requestSerialize: serialize_GetCinemaListRequest,
    requestDeserialize: deserialize_GetCinemaListRequest,
    responseSerialize: serialize_GetCinemaListResponse,
    responseDeserialize: deserialize_GetCinemaListResponse,
  },
  getMovieTimeslots: {
    path: '/EnquiryBot/getMovieTimeslots',
    requestStream: false,
    responseStream: false,
    requestType: control$plane_pb.GetMovieTimeslotsRequest,
    responseType: control$plane_pb.GetMovieTimeslotsResponse,
    requestSerialize: serialize_GetMovieTimeslotsRequest,
    requestDeserialize: deserialize_GetMovieTimeslotsRequest,
    responseSerialize: serialize_GetMovieTimeslotsResponse,
    responseDeserialize: deserialize_GetMovieTimeslotsResponse,
  },
};

exports.EnquiryBotClient = grpc.makeGenericClientConstructor(EnquiryBotService);
