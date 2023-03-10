from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List


@dataclass
class Provider(str, Enum):
    MCL = 'mcl-cinemas'


@dataclass
class Movie:
    id: str
    name: str
    provider: str


class MovieFetcher(ABC):

    @abstractmethod
    async def get_available_movie_list(self) -> List[Movie]:
        pass

    @property
    @abstractmethod
    def provider(self) -> Provider:
        pass
