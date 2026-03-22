from typing import List, Optional

from pydantic import BaseModel


class YoutubeVideoResponse(BaseModel):
    video_id: str
    title: str
    thumbnail_url: str
    channel_name: str
    published_at: str
    video_url: str


class YoutubeListResponse(BaseModel):
    items: List[YoutubeVideoResponse]
    next_page_token: Optional[str] = None
    prev_page_token: Optional[str] = None
    total_results: int
