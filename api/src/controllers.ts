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

export class GetMovieListController implements IController {
  async handle(req: express.Request, res: express.Response) {
    const rpcRequest = new GetAvailableMovieListRequest();
    const rpcResponse = (await promisify(client.getAvailableMovieList)(
      rpcRequest
    )) as GetAvailableMovieListResponse;
    res.send(rpcResponse.toObject().movieListList);
  }
}

export class GetMovieDetailController implements IController {
  async handle(req: express.Request, res: express.Response) {
    const rpcRequest = new GetMovieDetailsRequest();
    rpcRequest.setId(req.params.movieId);
    const rpcResponse = (await promisify(client.getMovieDetails)(
      rpcRequest
    )) as MovieDetail;
    res.send(rpcResponse.toObject());
  }
}

export class GetCinemaListController implements IController {
  async handle(req: express.Request, res: express.Response) {
    const rpcRequest = new GetCinemaListRequest();
    const rpcResponse = (await promisify(client.getCinemaList)(
      rpcRequest
    )) as GetCinemaListResponse;
    res.send(rpcResponse.toObject().cinemaListList);
  }
}

export class GetMovieTimeslotsController implements IController {
  async handle(req: express.Request, res: express.Response) {
    const rpcRequest = new GetMovieTimeslotsRequest();
    rpcRequest.setId(req.params.movieId);
    const rpcResponse = (await promisify(client.getMovieTimeslots)(
      rpcRequest
    )) as GetMovieTimeslotsResponse;
    res.send(rpcResponse.toObject().movieTimeslotsList);
  }
}
