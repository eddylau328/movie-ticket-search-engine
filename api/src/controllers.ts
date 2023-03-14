import express from "express";
import { promisify } from "util";
import {
  GetCinemaListRequest,
  GetCinemaListResponse,
  GetMovieDetailsRequest,
  GetMovieTimeslotsRequest,
  GetMovieTimeslotsResponse,
  Movie,
  MovieDetail,
} from "../grpc/control-plane_pb";
import cheerio from "cheerio";
import { client } from "./client";
import { formatDate } from "./helper";
import { IController } from "./types";
import fetch from "node-fetch";

function format<T>(
  data: T,
  pagination?: {
    total: number;
    current: number;
  }
) {
  return {
    data,
    pagination,
  };
}

const TMDB_URL = "https://api.themoviedb.org/3";
const TMDB_API_KEY = "dd3f63b423345f257e26262c3f650284";

export class SearchMovieWithTMDBController implements IController {
  async handle(
    req: express.Request,
    res: express.Response,
    next: express.NextFunction
  ) {
    try {
      const q = req.query.q;
      const searchResponse = await fetch(
        `${TMDB_URL}/search/movie?api_key=${TMDB_API_KEY}&query=${q}&language=zh-hk`
      );
      const searchResult = (await searchResponse.json()) as {
        results: Movie[];
      };
      res.send(format(searchResult.results[0]));
    } catch (err) {
      next(err);
    }
  }
}

export class GetMovieListController implements IController {
  async handle(
    req: express.Request,
    res: express.Response,
    next: express.NextFunction
  ) {
    try {
      const fetchResult = await fetch("https://wmoov.com/movie/showing");
      const html = await fetchResult.text();
      const $ = cheerio.load(html);
      const options = $('optgroup[label="上映中"] option');
      const movies = options.map((i, option) => ({
        name: $(option).text(),
      }));
      res.send(format(movies.toArray()));
    } catch (err) {
      next(err);
    }
  }
}

export class GetMovieDetailController implements IController {
  async handle(
    req: express.Request,
    res: express.Response,
    next: express.NextFunction
  ) {
    try {
      const rpcRequest = new GetMovieDetailsRequest();
      rpcRequest.setMovieName(req.params.movieName);
      const rpcResponse = (await promisify(client.getMovieDetail).bind(client)(
        rpcRequest
      )) as MovieDetail;
      res.send(format(rpcResponse.toObject()));
    } catch (err) {
      next(err);
    }
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
