export type ICinema = {
  id: string;
  name: string;
  provider: string;
  address: string;
  territory: string;
  district: string;
};

export type IMovie = {
  name: string;
};

export type IMovieTimeslot = {
  start: string;
  price: number;
  house: string;
  cinemaId: string;
  cinemaName: string;
  provider: string;
  movieName: string;
};

export type IMovieDetail = {
  id: string;
  name: string;
  provider: string;
  duration: number;
  rate: string;
  language: string;
  description: string;
};

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
