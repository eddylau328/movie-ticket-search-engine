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
const getCinemaListController = new GetCinemaListController();
const getMovieTimeslotsController = new GetMovieTimeslotsController();

app.get("/movies/:movieName/timeslots", (req, res) =>
  getMovieTimeslotsController.handle(req, res)
);
app.get("/movies/:movieName", (req, res) =>
  getMovieDetailController.handle(req, res)
);
app.get("/movies", (req, res) => getMovieListController.handle(req, res));
app.get("/cinemas", (req, res) => getCinemaListController.handle(req, res));

app.listen(8000);
