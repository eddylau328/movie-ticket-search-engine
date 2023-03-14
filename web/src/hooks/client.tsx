import { useState, useEffect } from "react";
import {
  fetchCinemas,
  fetchMovieDetail,
  fetchMovies,
  fetchMovieTimeslots,
  searchMovie,
} from "../fetch/client";
import { IMovie, ICinema, IMovieDetail, ITMDBMovie } from "../types/data.type";
import { uniqBy } from "lodash";
import { useAsync } from "react-use";

export function useMovies() {
  const [movies, setMovies] = useState<IMovie[]>([]);

  useEffect(() => {
    fetchMovies()
      .then((res) => res.data)
      .then((movies) =>
        uniqBy(movies, (m) => m.name.replace(/\s/g, "").split("(")[0])
      )
      .then((data) => setMovies(data));
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

export function useAsyncTimeslots(name: string) {
  const state = useAsync(async () => {
    const response = await fetchMovieTimeslots(name);
    return response.data;
  }, [name]);

  return state;
}

export function useTmdbMovie(name: string) {
  const [data, setData] = useState<ITMDBMovie>();

  useEffect(() => {
    searchMovie(name).then((data) => setData(data.data));
  }, [name]);

  return data;
}
