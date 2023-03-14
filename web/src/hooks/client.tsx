import { useState, useEffect } from "react";
import {
  fetchCinemas,
  fetchMovieDetail,
  fetchMovies,
  fetchMovieTimeslots,
  searchMovie,
} from "../fetch/client";
import {
  IMovie,
  ICinema,
  IMovieTimeslot,
  IMovieDetail,
  ITMDBMovie,
} from "../types/data.type";

export function useMovies() {
  const [movies, setMovies] = useState<IMovie[]>([]);

  useEffect(() => {
    fetchMovies().then((res) => setMovies(res.data));
  }, []);

  return movies;
}

export function useMovieDetails(name: string) {
  const [movie, setMovie] = useState<IMovieDetail>();

  useEffect(() => {
    fetchMovieDetail(name).then((res) => setMovie(res.data));
  }, [name]);

  return movie;
}

export function useCinemas() {
  const [cinemas, setCinemas] = useState<ICinema[]>([]);

  useEffect(() => {
    fetchCinemas().then((res) => setCinemas(res.data));
  }, []);

  return cinemas;
}

export function useTimeslots(name: string) {
  const [timeslots, setTimeslots] = useState<IMovieTimeslot[]>([]);

  useEffect(() => {
    fetchMovieTimeslots(name).then((res) => setTimeslots(res.data));
  }, [name]);

  return timeslots;
}

export function useTmdbMovie(name: string) {
  const [data, setData] = useState<ITMDBMovie>();

  useEffect(() => {
    searchMovie(name).then((data) => setData(data.data));
  }, [name]);

  return data;
}
