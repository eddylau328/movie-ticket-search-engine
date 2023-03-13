import express from "express";
import {
  GetMovieListController,
  GetMovieDetailController,
  GetCinemaListController,
  GetMovieTimeslotsController,
} from "./src/controllers";

const app = express();

const getMovieListController = new GetMovieListController();
const getMovieDetailController = new GetMovieDetailController();
const getTheaterListController = new GetCinemaListController();
const getMovieTimeslotsController = new GetMovieTimeslotsController();

app.get("/movies/:movieId/timeslots", (req, res) =>
  getMovieListController.handle(req, res)
);
app.get("/movies/:movieId", (req, res) =>
  getMovieDetailController.handle(req, res)
);
app.get("/movies", (req, res) => getTheaterListController.handle(req, res));
app.get("/theater", (req, res) => getMovieTimeslotsController.handle(req, res));

app.listen(8000);
