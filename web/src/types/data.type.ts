import { Cinema, Movie, MovieDetail, MovieTimeslot } from "../../../api/grpc";

export type ICinema = Cinema.AsObject;
export type IMovie = Movie.AsObject;
export type IMovieTimeslot = MovieTimeslot.AsObject;
export type IMovieDetail = MovieDetail.AsObject;
