import { useState, useEffect } from "react";
import {
  fetchCinemas,
  fetchMovieDetail,
  fetchMovies,
  fetchMovieTimeslots,
} from "../fetch";
import { IMovie, ICinema, IMovieTimeslot } from "../types/data.type";

export function useMovies() {
  const [movies, setMovies] = useState<IMovie[]>([]);

  useEffect(() => {
    fetchMovies().then((res) => setMovies(res.data));
  }, []);

  return movies;
}

export function useMovieDetails(name: string) {
  const [movie, setMovie] = useState<IMovie>();

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
