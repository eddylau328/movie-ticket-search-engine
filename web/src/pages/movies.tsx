import { Badge, Table } from "@mantine/core";
import { useMove } from "@mantine/hooks";
import { useNavigate } from "react-router-dom";
import { roundToNearestHalf } from "../helpers/numbers";
import { useMovies, useTmdbMovie } from "../hooks/client";
import { IMovie } from "../types/data.type";

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
  const movies = useMovies();
  const rows = movies.map((m) => <Row key={m.name} name={m.name} />);

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
