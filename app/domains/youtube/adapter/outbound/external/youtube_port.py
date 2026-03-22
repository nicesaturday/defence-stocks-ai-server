from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class YoutubeVideoItem:
    video_id: str
    title: str
    thumbnail_url: str
    channel_name: str
    published_at: str
    video_url: str


@dataclass
class YoutubeSearchResult:
    items: list[YoutubeVideoItem]
    next_page_token: Optional[str]
    prev_page_token: Optional[str]
    total_results: int


class YoutubePort(ABC):
    @abstractmethod
    def search_videos(self, query: str, max_results: int, page_token: Optional[str] = None) -> YoutubeSearchResult:
        pass
