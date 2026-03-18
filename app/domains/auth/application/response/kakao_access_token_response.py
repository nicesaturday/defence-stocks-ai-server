from pydantic import BaseModel


class KakaoAccessTokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int
    kakao_id: str
    nickname: str
    email: str
