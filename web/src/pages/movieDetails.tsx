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
import { useMovieDetails, useAsyncTimeslots } from "../hooks/client";
import { useTmdbMovie } from "../hooks/client";
import { IMovieTimeslot } from "../types/data.type";
import { useAsync } from "react-use";

function Row(props: IMovieTimeslot) {
  return (
    <tr>
      <td>{props.movieName}</td>
      <td>{props.provider}</td>
      <td>{props.house}</td>
      <td>{props.start}</td>
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

  const asyncTimeslot = useAsyncTimeslots(movieName ?? "");
  const timeslots = asyncTimeslot.value ?? [];

  const rows = timeslots.map((timeslot) => <Row {...timeslot} />);

  return (
    <Box>
      <Group align={"end"}>
        <Image maw={240} radius="md" src={poster} />
        <Stack>
          <Title color={"white"} order={1}>
            {movieName}
          </Title>
          <Text color={"white"}>{tmdb?.overview}</Text>
          <Rating
            value={(tmdb?.vote_average ?? 0) / 2}
            fractions={2}
            readOnly
          />
          ;
        </Stack>
      </Group>
      {asyncTimeslot.loading ? (
        <Text size={"lg"} color="white">
          Loading...
        </Text>
      ) : (
        <Table>
          <thead>
            <tr>
              <th>movie name</th>
              <th>provider</th>
              <th>house</th>
              <th>time</th>
              <th>price</th>
            </tr>
          </thead>
          <tbody>{rows}</tbody>
        </Table>
      )}
    </Box>
  );
}
