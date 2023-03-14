import { ITMDBMovie } from "../types/data.type";

const TMDB_URL = "https://api.themoviedb.org/3";
const TMDB_API_KEY = "dd3f63b423345f257e26262c3f650284";
const TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500";

export function getMovieUrl(name: string) {
  return `${TMDB_IMAGE_URL}${name}`;
}

export function searchMovie(name: string): Promise<ITMDBMovie> {
  return fetch(
    `${TMDB_URL}/search/movie?api_key=${TMDB_API_KEY}&query=${name}&language=zh-hk`
  )
    .then((response) => response.json())
    .then((data) => data.results[0]);
}
