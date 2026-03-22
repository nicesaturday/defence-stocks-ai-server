from typing import Optional

import httpx

from app.domains.youtube.adapter.outbound.external.youtube_port import (
    YoutubePort,
    YoutubeSearchResult,
    YoutubeVideoItem,
)
from app.infrastructure.config.settings import settings

YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"


class YoutubeClient(YoutubePort):
    def search_videos(self, query: str, max_results: int, page_token: Optional[str] = None) -> YoutubeSearchResult:
        params = {
            "part": "snippet",
            "q": query,
            "type": "video",
            "maxResults": max_results,
            "order": "date",
            "regionCode": "KR",
            "relevanceLanguage": "ko",
            "key": settings.youtube_api_key,
        }

        if page_token:
            params["pageToken"] = page_token

        response = httpx.get(YOUTUBE_SEARCH_URL, params=params)
        response.raise_for_status()
        data = response.json()

        items = [
            YoutubeVideoItem(
                video_id=item["id"]["videoId"],
                title=item["snippet"]["title"],
                thumbnail_url=item["snippet"]["thumbnails"]["high"]["url"],
                channel_name=item["snippet"]["channelTitle"],
                published_at=item["snippet"]["publishedAt"],
                video_url=f"https://www.youtube.com/watch?v={item['id']['videoId']}",
            )
            for item in data.get("items", [])
        ]

        return YoutubeSearchResult(
            items=items,
            next_page_token=data.get("nextPageToken"),
            prev_page_token=data.get("prevPageToken"),
            total_results=data.get("pageInfo", {}).get("totalResults", 0),
        )
