import express from "express";
import cors from "cors";
import {
  GetMovieListController,
  GetMovieDetailController,
  GetCinemaListController,
  GetMovieTimeslotsController,
  SearchMovieWithTMDBController,
} from "./src/controllers";

const app = express();

const searchMovieController = new SearchMovieWithTMDBController();
const getMovieListController = new GetMovieListController();
const getMovieDetailController = new GetMovieDetailController();
const getCinemaListController = new GetCinemaListController();
const getMovieTimeslotsController = new GetMovieTimeslotsController();

app.use(
  cors({
    origin: "http://localhost:3000",
  })
);

app.get("/movies/search", (req, res, next) =>
  searchMovieController.handle(req, res, next)
);
app.get("/movies/:movieName/timeslots", (req, res) =>
  getMovieTimeslotsController.handle(req, res)
);
app.get("/movies/:movieName", (req, res, next) =>
  getMovieDetailController.handle(req, res, next)
);
app.get("/movies", (req, res, next) =>
  getMovieListController.handle(req, res, next)
);
app.get("/cinemas", (req, res) => getCinemaListController.handle(req, res));

app.listen(8000);
