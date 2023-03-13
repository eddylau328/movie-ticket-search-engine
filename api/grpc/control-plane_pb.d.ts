// package: 
// file: control-plane.proto

import * as jspb from "google-protobuf";

export class Cinema extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  getName(): string;
  setName(value: string): void;

  getProvider(): ProviderMap[keyof ProviderMap];
  setProvider(value: ProviderMap[keyof ProviderMap]): void;

  getLocation(): string;
  setLocation(value: string): void;

  getTerritory(): TerritoryMap[keyof TerritoryMap];
  setTerritory(value: TerritoryMap[keyof TerritoryMap]): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Cinema.AsObject;
  static toObject(includeInstance: boolean, msg: Cinema): Cinema.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Cinema, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Cinema;
  static deserializeBinaryFromReader(message: Cinema, reader: jspb.BinaryReader): Cinema;
}

export namespace Cinema {
  export type AsObject = {
    id: string,
    name: string,
    provider: ProviderMap[keyof ProviderMap],
    location: string,
    territory: TerritoryMap[keyof TerritoryMap],
  }
}

export class Movie extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  getName(): string;
  setName(value: string): void;

  getProvider(): ProviderMap[keyof ProviderMap];
  setProvider(value: ProviderMap[keyof ProviderMap]): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Movie.AsObject;
  static toObject(includeInstance: boolean, msg: Movie): Movie.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Movie, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Movie;
  static deserializeBinaryFromReader(message: Movie, reader: jspb.BinaryReader): Movie;
}

export namespace Movie {
  export type AsObject = {
    id: string,
    name: string,
    provider: ProviderMap[keyof ProviderMap],
  }
}

export class MovieTimeslot extends jspb.Message {
  getStart(): string;
  setStart(value: string): void;

  getPrice(): number;
  setPrice(value: number): void;

  getLocation(): string;
  setLocation(value: string): void;

  getHouse(): string;
  setHouse(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MovieTimeslot.AsObject;
  static toObject(includeInstance: boolean, msg: MovieTimeslot): MovieTimeslot.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MovieTimeslot, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MovieTimeslot;
  static deserializeBinaryFromReader(message: MovieTimeslot, reader: jspb.BinaryReader): MovieTimeslot;
}

export namespace MovieTimeslot {
  export type AsObject = {
    start: string,
    price: number,
    location: string,
    house: string,
  }
}

export class MovieDetail extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  getName(): string;
  setName(value: string): void;

  getProvider(): ProviderMap[keyof ProviderMap];
  setProvider(value: ProviderMap[keyof ProviderMap]): void;

  getDuration(): number;
  setDuration(value: number): void;

  getRate(): string;
  setRate(value: string): void;

  getLanguage(): string;
  setLanguage(value: string): void;

  getDescription(): string;
  setDescription(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MovieDetail.AsObject;
  static toObject(includeInstance: boolean, msg: MovieDetail): MovieDetail.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MovieDetail, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MovieDetail;
  static deserializeBinaryFromReader(message: MovieDetail, reader: jspb.BinaryReader): MovieDetail;
}

export namespace MovieDetail {
  export type AsObject = {
    id: string,
    name: string,
    provider: ProviderMap[keyof ProviderMap],
    duration: number,
    rate: string,
    language: string,
    description: string,
  }
}

export class GetAvailableMovieListRequest extends jspb.Message {
  hasCinemaId(): boolean;
  clearCinemaId(): void;
  getCinemaId(): string;
  setCinemaId(value: string): void;

  hasCinemaProvider(): boolean;
  clearCinemaProvider(): void;
  getCinemaProvider(): ProviderMap[keyof ProviderMap];
  setCinemaProvider(value: ProviderMap[keyof ProviderMap]): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAvailableMovieListRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAvailableMovieListRequest): GetAvailableMovieListRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAvailableMovieListRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAvailableMovieListRequest;
  static deserializeBinaryFromReader(message: GetAvailableMovieListRequest, reader: jspb.BinaryReader): GetAvailableMovieListRequest;
}

export namespace GetAvailableMovieListRequest {
  export type AsObject = {
    cinemaId: string,
    cinemaProvider: ProviderMap[keyof ProviderMap],
  }
}

export class GetAvailableMovieListResponse extends jspb.Message {
  clearMovieListList(): void;
  getMovieListList(): Array<Movie>;
  setMovieListList(value: Array<Movie>): void;
  addMovieList(value?: Movie, index?: number): Movie;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAvailableMovieListResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetAvailableMovieListResponse): GetAvailableMovieListResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAvailableMovieListResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAvailableMovieListResponse;
  static deserializeBinaryFromReader(message: GetAvailableMovieListResponse, reader: jspb.BinaryReader): GetAvailableMovieListResponse;
}

export namespace GetAvailableMovieListResponse {
  export type AsObject = {
    movieListList: Array<Movie.AsObject>,
  }
}

export class GetMovieDetailsRequest extends jspb.Message {
  getMovieName(): string;
  setMovieName(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetMovieDetailsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetMovieDetailsRequest): GetMovieDetailsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetMovieDetailsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetMovieDetailsRequest;
  static deserializeBinaryFromReader(message: GetMovieDetailsRequest, reader: jspb.BinaryReader): GetMovieDetailsRequest;
}

export namespace GetMovieDetailsRequest {
  export type AsObject = {
    movieName: string,
  }
}

export class GetCinemaListRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCinemaListRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCinemaListRequest): GetCinemaListRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCinemaListRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCinemaListRequest;
  static deserializeBinaryFromReader(message: GetCinemaListRequest, reader: jspb.BinaryReader): GetCinemaListRequest;
}

export namespace GetCinemaListRequest {
  export type AsObject = {
  }
}

export class GetCinemaListResponse extends jspb.Message {
  clearCinemaListList(): void;
  getCinemaListList(): Array<Cinema>;
  setCinemaListList(value: Array<Cinema>): void;
  addCinemaList(value?: Cinema, index?: number): Cinema;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCinemaListResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetCinemaListResponse): GetCinemaListResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCinemaListResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCinemaListResponse;
  static deserializeBinaryFromReader(message: GetCinemaListResponse, reader: jspb.BinaryReader): GetCinemaListResponse;
}

export namespace GetCinemaListResponse {
  export type AsObject = {
    cinemaListList: Array<Cinema.AsObject>,
  }
}

export class GetMovieTimeslotsRequest extends jspb.Message {
  getMovieName(): string;
  setMovieName(value: string): void;

  getPriceLte(): number;
  setPriceLte(value: number): void;

  getPriceGte(): number;
  setPriceGte(value: number): void;

  getTimeLte(): string;
  setTimeLte(value: string): void;

  getTimeGte(): string;
  setTimeGte(value: string): void;

  getDistrict(): DistrictMap[keyof DistrictMap];
  setDistrict(value: DistrictMap[keyof DistrictMap]): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetMovieTimeslotsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetMovieTimeslotsRequest): GetMovieTimeslotsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetMovieTimeslotsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetMovieTimeslotsRequest;
  static deserializeBinaryFromReader(message: GetMovieTimeslotsRequest, reader: jspb.BinaryReader): GetMovieTimeslotsRequest;
}

export namespace GetMovieTimeslotsRequest {
  export type AsObject = {
    movieName: string,
    priceLte: number,
    priceGte: number,
    timeLte: string,
    timeGte: string,
    district: DistrictMap[keyof DistrictMap],
  }
}

export class GetMovieTimeslotsResponse extends jspb.Message {
  clearMovieTimeslotsList(): void;
  getMovieTimeslotsList(): Array<MovieTimeslot>;
  setMovieTimeslotsList(value: Array<MovieTimeslot>): void;
  addMovieTimeslots(value?: MovieTimeslot, index?: number): MovieTimeslot;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetMovieTimeslotsResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetMovieTimeslotsResponse): GetMovieTimeslotsResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetMovieTimeslotsResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetMovieTimeslotsResponse;
  static deserializeBinaryFromReader(message: GetMovieTimeslotsResponse, reader: jspb.BinaryReader): GetMovieTimeslotsResponse;
}

export namespace GetMovieTimeslotsResponse {
  export type AsObject = {
    movieTimeslotsList: Array<MovieTimeslot.AsObject>,
  }
}

export interface ProviderMap {
  MCL: 0;
}

export const Provider: ProviderMap;

export interface DistrictMap {
  ISLANDS: 0;
  KWAI_TSING: 1;
  NORTH: 2;
  SAI_KUNG: 3;
  SHA_TIN: 4;
  TAI_PO: 5;
  TSUEN_WAN: 6;
  TUEN_MUN: 7;
  YUEN_LONG: 8;
  KOWLOON_CITY: 9;
  KWUN_TONG: 10;
  SHAM_SHUI_PO: 11;
  WONG_TAI_SIN: 12;
  YAU_TSIM_MONG: 13;
  CENTRAL_AND_WESTERN: 14;
  EASTERN: 15;
  SOUTHERN: 16;
  WAN_CHAI: 17;
}

export const District: DistrictMap;

export interface TerritoryMap {
  KOWLOON: 0;
  NEW_TERRITORIES: 1;
  HONG_KONG_ISLAND: 2;
}

export const Territory: TerritoryMap;

