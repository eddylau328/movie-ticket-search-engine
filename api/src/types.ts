import express from "express";

export interface IController {
  handle(
    req: express.Request,
    res: express.Response,
    next?: express.NextFunction
  ): Promise<void>;
}
