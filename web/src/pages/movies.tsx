import { Badge, Table } from "@mantine/core";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { roundToNearestHalf } from "../helpers/numbers";
import { useTmdbMovie } from "../hooks/tmdb";
import { IMovie } from "../types/data.type";

const mockMovies: IMovie[] = [
  {
    id: "",
    name: "鈴芽之旅",
    provider: 0,
  },
  {
    id: "",
    name: "毒舌大狀",
    provider: 0,
  },
  {
    id: "",
    name: "65：絕境逃生",
    provider: 0,
  },
  {
    id: "",
    name: "奪命狂呼6",
    provider: 0,
  },
  {
    id: "",
    name: "殺神John Wick 4",
    provider: 0,
  },
];

function getColor(rating: number) {
  if (rating < 5) return "red";
  if (rating < 7) return "yellow";
  return "green";
}

function Row({ name }: { name: string }) {
  const tmdb = useTmdbMovie(name);
  const navigate = useNavigate();
  return (
    <tr
      className="clickable"
      key={name}
      onClick={() => navigate(`/movies/${name}`)}
    >
      <td>{name}</td>
      <td>
        {tmdb?.vote_average ? (
          <Badge color={getColor(tmdb?.vote_average)}>
            {roundToNearestHalf(tmdb?.vote_average ?? 0)}
          </Badge>
        ) : (
          <Badge color={"gray"}>N/A</Badge>
        )}
      </td>
      <td>{tmdb?.release_date}</td>
    </tr>
  );
}

export default function MoviesPage() {
  const rows = mockMovies.map((m) => <Row key={m.name} name={m.name} />);

  return (
    <div>
      <Table>
        <thead>
          <tr>
            <th>#</th>
            <th>vote</th>
            <th>release date</th>
          </tr>
        </thead>
        <tbody>{rows}</tbody>
      </Table>
    </div>
  );
}
