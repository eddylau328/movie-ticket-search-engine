import {
  IMovie,
  IMovieDetail,
  ICinema,
  IMovieTimeslot,
} from "../types/data.type";

import { Response } from "../types/response.type";

const BASE_URL = "http://localhost:8000";

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
