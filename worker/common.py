from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional


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

    @classmethod
    def map_address(cls, address: str) -> Optional[District]:
        def check(addr: str, areas: List[str]) -> bool:
            return any(area.lower() in addr.lower() for area in areas)
        for districts in AREAS_MAP.values():
            for district, areas in districts.items():
                if check(address, areas['zh']) or check(address, areas['en']):
                    return district
        return None


class Territory(str, Enum):
    KOWLOON = 'kowloon'
    NEW_TERRITORIES = 'new-territories'
    HONG_KONG_ISLAND = 'hong-kong-island'

    @classmethod
    def map_address(cls, address: str) -> Optional[Territory]:
        def check(addr: str, areas: List[str]) -> bool:
            return any(area.lower() in addr.lower() for area in areas)
        for territory, districts in AREAS_MAP.items():
            for areas in districts.values():
                if check(address, areas['zh']) or check(address, areas['en']):
                    return territory
        return None


AREAS_MAP = {
    Territory.NEW_TERRITORIES: {
        District.CENTRAL_AND_WESTERN: {
            'zh': [
                '堅尼地城',
                '石塘咀',
                '西營盤',
                '上環',
                '中環',
                '金鐘',
                '半山區',
                '山頂',
            ],
            'en': [
                'Kennedy Town',
                'Shek Tong Tsui',
                'Sai Ying Pun',
                'Sheung Wan',
                'Central',
                'Admiralty',
                'Mid-levels',
                'Peak',
            ],
        },
        District.WAN_CHAI: {
            'zh': [
                '灣仔',
                '銅鑼灣',
                '跑馬地',
                '大坑',
                '掃桿埔',
                '渣甸山',
            ],
            'en': [
                'Wan Chai',
                'Causeway Bay',
                'Happy Valley',
                'Tai Hang',
                'So Kon Po',
                'Jardine\'s Lookout'
            ],
        },
        District.EASTERN: {
            'zh': [
                '天后',
                '寶馬山',
                '北角',
                '鰂魚涌',
                '西灣河',
                '筲箕灣',
                '柴灣',
                '小西灣',
            ],
            'en': [
                'Tin Hau',
                'Braemar Hill',
                'North Point',
                'Quarry Bay',
                'Sai Wan Ho',
                'Shau Kei Wan',
                'Chai Wan',
                'Siu Sai Wan',
            ],
        },
        District.SOUTHERN: {
            'zh': [
                '薄扶林', '香港仔',
                '鴨脷洲', '黃竹坑',
                '壽臣山', '淺水灣',
                '舂磡角', '赤柱',
                '大潭', '石澳',
            ],
            'en': [
                'Pok Fu Lam', 'Aberdeen',
                'Ap Lei Chau', 'Wong Chuk Hang',
                'Shouson Hill', 'Repulse Bay',
                'Chung Hom Kok', 'Stanley',
                'Tai Tam', 'Shek O',
            ],
        },
    },
    Territory.KOWLOON: {
        District.YAU_TSIM_MONG: {
            'zh': [
                '尖沙咀', '油麻地',
                '西九龍填海區',
                '京士柏', '旺角',
                '大角咀',
            ],
            'en': [
                'Tsim Sha Tsui', 'Yau Ma Tei',
                'West Kowloon Reclamation',
                'King\'s Park', 'Mong Kok',
                'Tai Kok Tsui',
            ],
        },
        District.SHAM_SHUI_PO: {
            'zh': [
                '美孚', '荔枝角',
                '長沙灣',
                '深水埗', '石硤尾',
                '又一村', '大窩坪',
                '昂船洲',
            ],
            'en': [
                'Mei Foo', 'Lai Chi Kok',
                'Cheung Sha Wan',
                'Sham Shui Po', 'Shek Kip Mei',
                'Yau Yat Tsuen', 'Tai Wo Ping',
                'Stonecutters Island',
            ],
        },
        District.KOWLOON_CITY: {
            'zh': [
                '紅磡', '土瓜灣',
                '馬頭角', '馬頭圍',
                '啟德', '九龍城',
                '何文田', '九龍塘',
                '筆架山',
            ],
            'en': [
                'Hung Hom', 'To Kwa Wan',
                'Ma Tau Kok', 'Ma Tau Wai',
                'Kai Tak', 'Kowloon City',
                'Ho Man Tin', 'Kowloon Tong',
                'Beacon Hill',
            ],
        },
        District.WONG_TAI_SIN: {
            'zh': [
                '新蒲崗', '黃大仙',
                '東頭', '橫頭磡',
                '樂富', '鑽石山',
                '慈雲山', '牛池灣',
            ],
            'en': [
                'San Po Kong', 'Wong Tai Sin',
                'Tung Tau', 'Wang Tau Hom',
                'Lok Fu', 'Diamond Hill',
                'Tsz Wan Shan', 'Ngau Chi Wan',
            ],
        },
        District.KWUN_TONG: {
            'zh': [
                '坪石', '九龍灣',
                '牛頭角', '佐敦谷',
                '觀塘', '秀茂坪',
                '藍田', '油塘',
                '鯉魚門',
            ],
            'en': [
                'Ping Shek', 'Kowloon Bay',
                'Ngau Tau Kok', 'Jordan Valley',
                'Kwun Tong', 'Sau Mau Ping',
                'Lam Tin', 'Yau Tong',
                'Lei Yue Mun',
            ],
        },
    },
    Territory.NEW_TERRITORIES: {
        District.KWAI_TSING: {
            'zh': [
                '葵涌', '青衣',
            ],
            'en': [
                'Kwai Chung', 'Tsing Yi',
            ],
        },
        District.TSUEN_WAN: {
            'zh': [
                '荃灣', '梨木樹',
                '汀九', '深井',
                '青龍頭', '馬灣',
                '欣澳',
            ],
            'en': [
                'Tsuen Wan', 'Lei Muk Shue',
                'Ting Kau', 'Sham Tseng',
                'Tsing Lung Tau', 'Ma Wan',
                'Sunny Bay',
            ],
        },
        District.TUEN_MUN: {
            'zh': [
                '大欖涌',
                '掃管笏',
                '屯門', '藍地',
            ],
            'en': [
                'Tai Lam Chung',
                'So Kwun Wat',
                'Tuen Mun', 'Lam Tei',
            ],
        },
        District.YUEN_LONG: {
            'zh': [
                '洪水橋', '廈村',
                '流浮山',
                '天水圍', '元朗',
                '新田', '落馬洲',
                '錦田', '石崗',
                '八鄉',
            ],
            'en': [
                'Hung Shui Kiu', 'Ha Tsuen',
                'Lau Fau Shan',
                'Tin Shui Wai', 'Yuen Long',
                'San Tin', 'Lok Ma Chau',
                'Kam Tin', 'Shek Kong',
                'Pat Heung',
            ],
        },
        District.NORTH: {
            'zh': [
                '粉嶺', '聯和墟',
                '上水',
                '石湖墟',
                '沙頭角', '鹿頸',
                '烏蛟騰',
            ],
            'en': [
                'Fanling', 'Luen Wo Hui',
                'Sheung Shui',
                'Shek Wu Hui',
                'Sha Tau Kok', 'Luk Keng',
                'Wu Kau Tang',
            ],
        },
        District.TAI_PO: {
            'zh': [
                '大埔墟', '大埔',
                '大埔滘', '大尾篤',
                '船灣',
                '樟木頭',
                '企嶺下'
            ],
            'en': [
                'Tai Po Market', 'Tai Po',
                'Tai Po Kau', 'Tai Mei Tuk',
                'Shuen Wan',
                'Cheung Muk Tau',
                'Kei Ling Ha',
            ],
        },
        District.SHA_TIN: {
            'zh': [
                '大圍', '沙田',
                '火炭', '馬料水',
                '烏溪沙',
                '馬鞍山'
            ],
            'en': [
                'Tai Wai', 'Sha Tin',
                'Fo Tan', 'Ma Liu Shui',
                'Wu Kai Sha',
                'Ma On Shan',
            ],
        },
        District.SAI_KUNG: {
            'zh': [
                '清水灣', '西貢',
                '大網仔',
                '將軍澳',
                '坑口', '調景嶺',
                '馬游塘',
            ],
            'en': [
                'Clear Water Bay', 'Sai Kung',
                'Tai Mong Tsai',
                'Tseung Kwan O',
                'Hang Hau', 'Tiu Keng Leng',
                'Ma Yau Tong'
            ],
        },
        District.ISLANDS: {
            'zh': [
                '長洲', '坪洲',
                '大嶼山', '東涌',
                '南丫島',
            ],
            'en': [
                'Cheung Chau', 'Peng Chau',
                'Lantau Islanda', 'Tung Chung',
                'Lamma Island',
            ],
        },
    },
}


@dataclass
class Cinema:
    id: str
    name: str
    provider: Provider
    address: str
    district: District
    territory: Territory

    def dict(self) -> Dict[str, str]:
        res = asdict(self)
        res['provider'] = self.provider.value
        res['district'] = self.district.value
        res['territory'] = self.territory.value
        return res


@dataclass
class Movie:
    id: str
    name: str

    def dict(self) -> Dict[str, str]:
        res = asdict(self)
        return res


@dataclass
class MovieDetail(Movie):
    duration: int
    rate: str
    language: str
    description: str


@dataclass
class MovieTimeslot:
    start: datetime  # ISO8601 format in hong kong timezone, no datetime if using gRPC
    price: float
    cinema_id: str
    cinema_name: str
    provider: Provider
    house: str

    def dict(self) -> Dict[str, str]:
        res = asdict(self)
        res['provider'] = self.provider.value
        res['start'] = self.start.isoformat()
        return res


class EnquiryBot(ABC):

    async def get_movie_details(self, id: str) -> Optional[MovieDetail]:
        """
        Provide description about the movie 
        """
        return None

    async def get_movie_timeslots(self, movie_id: str, **kwargs) -> List[MovieTimeslot]:
        """
        Provide timeslots of that day in different places

        kwargs
        - price_lte: float  # less than equal
        - price_gte: float  # greater than equal
        - time_lte: str     # less than equal
        - time_gte: str     # greater than equal
        - district: District
        """
        return []

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
    async def get_cinema_list(self) -> List[Cinema]:
        """
        Provide a list of cinemas in Hong Kong
        """
        pass

    @property
    @abstractmethod
    def provider(self) -> Provider:
        pass
