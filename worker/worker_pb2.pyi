from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

CENTRAL_AND_WESTERN: District
DESCRIPTOR: _descriptor.FileDescriptor
EASTERN: District
GOLDEN_HARVEST: Provider
HONG_KONG_ISLAND: Territory
ISLANDS: District
KOWLOON: Territory
KOWLOON_CITY: District
KWAI_TSING: District
KWUN_TONG: District
MCL: Provider
NEW_TERRITORIES: Territory
NORTH: District
SAI_KUNG: District
SHAM_SHUI_PO: District
SHA_TIN: District
SOUTHERN: District
TAI_PO: District
TSUEN_WAN: District
TUEN_MUN: District
WAN_CHAI: District
WONG_TAI_SIN: District
YAU_TSIM_MONG: District
YUEN_LONG: District

class Cinema(_message.Message):
    __slots__ = ["id", "location", "name", "provider", "territory"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_FIELD_NUMBER: _ClassVar[int]
    id: str
    location: str
    name: str
    provider: Provider
    territory: Territory
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., provider: _Optional[_Union[Provider, str]] = ..., location: _Optional[str] = ..., territory: _Optional[_Union[Territory, str]] = ...) -> None: ...

class GetAvailableMovieListRequest(_message.Message):
    __slots__ = ["cinema_id", "cinema_provider"]
    CINEMA_ID_FIELD_NUMBER: _ClassVar[int]
    CINEMA_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    cinema_id: str
    cinema_provider: Provider
    def __init__(self, cinema_id: _Optional[str] = ..., cinema_provider: _Optional[_Union[Provider, str]] = ...) -> None: ...

class GetAvailableMovieListResponse(_message.Message):
    __slots__ = ["movie_list"]
    MOVIE_LIST_FIELD_NUMBER: _ClassVar[int]
    movie_list: _containers.RepeatedCompositeFieldContainer[Movie]
    def __init__(self, movie_list: _Optional[_Iterable[_Union[Movie, _Mapping]]] = ...) -> None: ...

class GetCinemaListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetCinemaListResponse(_message.Message):
    __slots__ = ["cinema_list"]
    CINEMA_LIST_FIELD_NUMBER: _ClassVar[int]
    cinema_list: _containers.RepeatedCompositeFieldContainer[Cinema]
    def __init__(self, cinema_list: _Optional[_Iterable[_Union[Cinema, _Mapping]]] = ...) -> None: ...

class GetMovieDetailsRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetMovieTimeslotsRequest(_message.Message):
    __slots__ = ["district", "movie_name", "price_gte", "price_lte", "time_gte", "time_lte"]
    DISTRICT_FIELD_NUMBER: _ClassVar[int]
    MOVIE_NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_GTE_FIELD_NUMBER: _ClassVar[int]
    PRICE_LTE_FIELD_NUMBER: _ClassVar[int]
    TIME_GTE_FIELD_NUMBER: _ClassVar[int]
    TIME_LTE_FIELD_NUMBER: _ClassVar[int]
    district: District
    movie_name: str
    price_gte: float
    price_lte: float
    time_gte: str
    time_lte: str
    def __init__(self, movie_name: _Optional[str] = ..., price_lte: _Optional[float] = ..., price_gte: _Optional[float] = ..., time_lte: _Optional[str] = ..., time_gte: _Optional[str] = ..., district: _Optional[_Union[District, str]] = ...) -> None: ...

class GetMovieTimeslotsResponse(_message.Message):
    __slots__ = ["movie_timeslots"]
    MOVIE_TIMESLOTS_FIELD_NUMBER: _ClassVar[int]
    movie_timeslots: _containers.RepeatedCompositeFieldContainer[MovieTimeslot]
    def __init__(self, movie_timeslots: _Optional[_Iterable[_Union[MovieTimeslot, _Mapping]]] = ...) -> None: ...

class Movie(_message.Message):
    __slots__ = ["id", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class MovieDetail(_message.Message):
    __slots__ = ["description", "duration", "id", "language", "name", "provider", "rate"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    description: str
    duration: int
    id: str
    language: str
    name: str
    provider: Provider
    rate: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., provider: _Optional[_Union[Provider, str]] = ..., duration: _Optional[int] = ..., rate: _Optional[str] = ..., language: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class MovieTimeslot(_message.Message):
    __slots__ = ["house", "location", "price", "start"]
    HOUSE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    house: str
    location: str
    price: float
    start: str
    def __init__(self, start: _Optional[str] = ..., price: _Optional[float] = ..., location: _Optional[str] = ..., house: _Optional[str] = ...) -> None: ...

class Provider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class District(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Territory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
