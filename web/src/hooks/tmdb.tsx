import { useEffect, useState } from "react";
import { searchMovie } from "../fetch/tmdb";
import { ITMDBMovie } from "../types/data.type";

export function useTmdbMovie(name: string) {
  const [data, setData] = useState<ITMDBMovie>();

  useEffect(() => {
    searchMovie(name).then((data) => setData(data));
  }, [name]);

  return data;
}
