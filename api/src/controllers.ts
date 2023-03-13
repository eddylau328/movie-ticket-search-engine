import express from "express";
import { promisify } from "util";
import {
  GetAvailableMovieListRequest,
  GetAvailableMovieListResponse,
  GetCinemaListRequest,
  GetCinemaListResponse,
  GetMovieDetailsRequest,
  GetMovieTimeslotsRequest,
  GetMovieTimeslotsResponse,
  MovieDetail,
} from "../grpc/control-plane_pb";
import { client } from "./client";
import { IController } from "./types";

function format<T>(data: T) {
  return {
    data,
  };
}

export class GetMovieListController implements IController {
  async handle(req: express.Request, res: express.Response) {
    const rpcRequest = new GetAvailableMovieListRequest();
    const rpcResponse = (await promisify(client.getAvailableMovieList).bind(
      client
    )(rpcRequest)) as GetAvailableMovieListResponse;
    res.send(format(rpcResponse.toObject().movieListList));
  }
}

export class GetMovieDetailController implements IController {
  async handle(req: express.Request, res: express.Response) {
    const rpcRequest = new GetMovieDetailsRequest();
    rpcRequest.setMovieName(req.params.movieName);
    const rpcResponse = (await promisify(client.getMovieDetail).bind(client)(
      rpcRequest
    )) as MovieDetail;
    res.send(format(rpcResponse.toObject()));
  }
}

export class GetCinemaListController implements IController {
  async handle(req: express.Request, res: express.Response) {
    const rpcRequest = new GetCinemaListRequest();
    const rpcResponse = (await promisify(client.getCinemaList).bind(client)(
      rpcRequest
    )) as GetCinemaListResponse;
    res.send(format(rpcResponse.toObject().cinemaListList));
  }
}

export class GetMovieTimeslotsController implements IController {
  async handle(req: express.Request, res: express.Response) {
    const rpcRequest = new GetMovieTimeslotsRequest();
    rpcRequest.setMovieName(req.params.movieName);
    const rpcResponse = (await promisify(client.getMovieTimeslots).bind(client)(
      rpcRequest
    )) as GetMovieTimeslotsResponse;
    res.send(format(rpcResponse.toObject().movieTimeslotsList));
  }
}
