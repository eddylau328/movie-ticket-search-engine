import express from "express";
import { IController } from "./types";

export class GetMovieListController implements IController {
  async handle(req: express.Request, res: express.Response) {
    res.send([]);
  }
}

export class GetMovieDetailController implements IController {
  async handle(req: express.Request, res: express.Response) {
    res.send({});
  }
}

export class GetTheaterListController implements IController {
  async handle(req: express.Request, res: express.Response) {
    res.send([]);
  }
}

export class GetMovieTimeslotsController implements IController {
  async handle(req: express.Request, res: express.Response) {
    res.send({});
  }
}
