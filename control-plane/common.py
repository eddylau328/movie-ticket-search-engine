from enum import Enum
from dataclasses import dataclass
from typing import Optional, List


class Provider(str, Enum):
    MCL = 'mcl-cinemas'
    GOLDEN_HARVEST = 'golden-harvest'


class District(str, Enum):
    ISLANDS = 'islands'
    KWAI_TSING = 'kwai-tsing'
    NORTH = 'north'
    SAI_KUNG = 'sai-kung'
    SHA_TIN = 'sha-tin'
    TAI_PO = 'tai-po'
    TSUEN_WAN = 'tsuen-wan'
    TUEN_MUN = 'tuen-mun'
    YUEN_LONG = 'yuen-long'
    KOWLOON_CITY = 'kowloon-city'
    KWUN_TONG = 'kwun-tong'
    SHAM_SHUI_PO = 'sham-shui-po'
    WONG_TAI_SIN = 'wong-tai-sin'
    YAU_TSIM_MONG = 'yau-tsim-mong'
    CENTRAL_AND_WESTERN = 'central-and-western'
    EASTERN = 'eastern'
    SOUTHERN = 'southern'
    WAN_CHAI = 'wan-chai'


class Territory(str, Enum):
    KOWLOON = 'kowloon'
    NEW_TERRITORIES = 'new-territories'
    HONG_KONG_ISLAND = 'hong-kong-island'


@dataclass
class Cinema:
    id: str
    name: str
    address: str
    provider: Provider
    district: District
    territory: Territory


@dataclass
class Movie:
    id: str
    name: str


@dataclass
class MovieDetail(Movie):
    duration: int
    rate: str
    language: str
    description: str


@dataclass
class MovieTimeslot:
    start: str  # ISO8601 format in hong kong timezone, no datetime if using gRPC
    price: float
    cinema_id: str
    cinema_name: str
    provider: Provider
    house: str


class EnquiryBotInterface:

    async def getMovieDetails(self, id: str) -> Optional[MovieDetail]:
        """
        Provide description about the movie 
        """
        raise NotImplementedError

    async def getMovieTimeslots(self, movie_id: str, **kwargs) -> List[MovieTimeslot]:
        """
        Provide timeslots of that day in different places

        kwargs
        - price_lte: float  # less than equal
        - price_gte: float  # greater than equal
        - time_lte: str     # less than equal
        - time_gte: str     # greater than equal
        - district: District
        """
        raise NotImplementedError

    async def getAvailableMovieList(self, **kwargs) -> List[Movie]:
        """
        Provide list of movies that is available to watch

        kwargs
        - cinema_id         : need to provide for cinema_provider
        - cinema_provider   : need to provide with cinema_id
        """
        raise NotImplementedError

    async def getCinemaList(self) -> List[Cinema]:
        """
        Provide a list of cinemas in Hong Kong
        """
        raise NotImplementedError
