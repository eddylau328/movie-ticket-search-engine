import { Cinema, Movie, MovieDetail, MovieTimeslot } from "../../../api/grpc";

export type ICinema = Cinema.AsObject;
export type IMovie = Movie.AsObject;
export type IMovieTimeslot = MovieTimeslot.AsObject;
export type IMovieDetail = MovieDetail.AsObject;
export type ITMDBMovie = {
  adult: boolean;
  backdrop_path: string;
  id: number;
  overview: string;
  popularity: number;
  poster_path: string;
  release_date: string;
  vote_average: number;
};
