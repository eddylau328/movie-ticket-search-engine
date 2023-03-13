from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List


class Provider(str, Enum):
    MCL = 'mcl-cinemas'


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
    provider: str
    location: str
    territory: str


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


class EnquiryBot(ABC):
    @abstractmethod
    async def get_available_movie_list(self, **kwargs) -> List[Movie]:
        """
        Provide list of movies that is available to watch

        kwargs
        - cinema_id         : need to provide for cinema_provider
        - cinema_provider   : need to provide with cinema_id
        """
        pass

    @abstractmethod
    async def get_movie_details(self, id: str) -> MovieDetail:
        """
        Provide description about the movie 
        """
        pass

    @abstractmethod
    async def get_cinema_list(self) -> List[Cinema]:
        """
        Provide a list of cinemas in Hong Kong
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
