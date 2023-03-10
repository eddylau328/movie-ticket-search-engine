from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List


@dataclass
class Provider(str, Enum):
    MCL = 'mcl-cinemas'


@dataclass
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


@dataclass
class Movie:
    id: str
    name: str
    provider: str


@dataclass
class MovieTimeslot:
    start: str  # ISO8601 format, no datetime if using gRPC
    price: float
    location: str
    house: str


@dataclass
class MovieDetail(Movie):
    duration: int
    rate: str
    language: str
    description: str


class MovieFetcher(ABC):

    @abstractmethod
    async def get_available_movie_list(self) -> List[Movie]:
        """
        Provide list of movies that is available to watch
        """
        pass

    @abstractmethod
    async def get_movie_details(self, id: str) -> MovieDetail:
        """
        Provide description about the movie 
        """
        pass

    @abstractmethod
    async def get_movie_timeslots(self, id: str, **kwargs) -> List[MovieTimeslot]:
        """
        Provide timeslots of that day in different places

        kwargs
        - price_lte: float  # less than equal
        - price_gte: float  # greater than equal
        - time_lte: str     # less than equal
        - time_gte: str     # greater than equal
        - district: District
        """
        pass

    @property
    @abstractmethod
    def provider(self) -> Provider:
        pass
