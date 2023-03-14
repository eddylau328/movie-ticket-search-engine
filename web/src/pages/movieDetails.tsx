import {
  Box,
  Text,
  Image,
  Title,
  Rating,
  Table,
  Group,
  Stack,
} from "@mantine/core";
import { useParams } from "react-router-dom";
import { getMovieUrl } from "../fetch/client";
import { useMovieDetails, useTimeslots } from "../hooks/client";
import { useTmdbMovie } from "../hooks/client";
import { IMovieTimeslot } from "../types/data.type";

const mockMovieTimeslots = [
  {
    start: "10:00",
    price: 200,
    location: "Cinema 1",
    house: "House 1",
  },
  {
    start: "12:15",
    price: 200,
    location: "Cinema 1",
    house: "House 1",
  },
  {
    start: "14:50",
    price: 200,
    location: "Cinema 1",
    house: "House 1",
  },
  {
    start: "15:00",
    price: 200,
    location: "Cinema 1",
    house: "House 1",
  },
  {
    start: "18:00",
    price: 200,
    location: "Cinema 1",
    house: "House 1",
  },
  {
    start: "20:00",
    price: 200,
    location: "Cinema 1",
    house: "House 1",
  },
];

function Row(props: IMovieTimeslot) {
  return (
    <tr>
      <td>{props.house}</td>
      <td>{props.start}</td>
      <td>{props.location}</td>
      <td>{props.price} HKD</td>
    </tr>
  );
}

export default function MovieDetailsPage() {
  const params = useParams();
  const movieName = params.movieName;

  const movieDetail = useMovieDetails(movieName ?? "");
  const tmdb = useTmdbMovie(movieName ?? "");
  const poster = getMovieUrl(tmdb?.poster_path ?? "");
  // const timeslots = useTimeslots(movieName ?? "");
  const timeslots = mockMovieTimeslots;

  const rows = timeslots.map((timeslot) => <Row {...timeslot} />);

  return (
    <Box>
      <Group align={"end"}>
        <Image maw={240} radius="md" src={poster} />
        <Stack>
          <Title color={"white"} order={1}>
            {movieDetail?.name ?? movieName}
          </Title>
          <Text color={"white"}>
            {movieDetail?.description ?? tmdb?.overview}
          </Text>
          <Rating
            value={(tmdb?.vote_average ?? 0) / 2}
            fractions={2}
            readOnly
          />
          ;
        </Stack>
      </Group>
      <Table>
        <thead>
          <tr>
            <th>house</th>
            <th>time</th>
            <th>location</th>
            <th>price</th>
          </tr>
        </thead>
        <tbody>{rows}</tbody>
      </Table>
    </Box>
  );
}
