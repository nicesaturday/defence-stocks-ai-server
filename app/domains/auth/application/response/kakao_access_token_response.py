from typing import Optional

from pydantic import BaseModel


class KakaoAccessTokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int
    kakao_id: str
    nickname: str
    email: str
    is_registered: bool
    account_id: Optional[int] = None
