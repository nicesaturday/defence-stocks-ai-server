from pydantic import BaseModel


class KakaoOauthUrlResponse(BaseModel):
    oauth_url: str
