import {
  IMovie,
  IMovieDetail,
  ICinema,
  IMovieTimeslot,
  ITMDBMovie,
} from "../types/data.type";

import { Response } from "../types/response.type";

const BASE_URL = "http://localhost:8000";
const TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500";

export function fetchMovies(): Promise<Response<IMovie[]>> {
  return fetch(`${BASE_URL}/movies`).then((response) => response.json());
}

export function fetchMovieDetail(
  name: string
): Promise<Response<IMovieDetail>> {
  return fetch(`${BASE_URL}/movies/${name}`).then((response) =>
    response.json()
  );
}

export function fetchCinemas(): Promise<Response<ICinema[]>> {
  return fetch(`${BASE_URL}/cinemas`).then((response) => response.json());
}

export function fetchMovieTimeslots(
  name: string
): Promise<Response<IMovieTimeslot[]>> {
  return fetch(`${BASE_URL}/movies/${name}/timeslots`).then((response) =>
    response.json()
  );
}

export function searchMovie(name: string): Promise<Response<ITMDBMovie>> {
  const parsedName = name.split("(")[0];
  return fetch(`${BASE_URL}/movies/search?q=${parsedName}`).then((response) =>
    response.json()
  );
}

export function getMovieUrl(name: string) {
  return `${TMDB_IMAGE_URL}${name}`;
}
