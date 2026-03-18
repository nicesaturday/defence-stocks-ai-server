from urllib.parse import urlencode

import httpx

from app.domains.auth.adapter.outbound.external.kakao_auth_port import KakaoAuthPort, KakaoTokenInfo, KakaoUserInfo
from app.infrastructure.config.settings import settings


class KakaoAuthClient(KakaoAuthPort):
    def get_kakao_access_token(self, authorization_code: str) -> KakaoTokenInfo:
        response = httpx.post(
            "https://kauth.kakao.com/oauth/token",
            data={
                "grant_type": "authorization_code",
                "client_id": settings.kakao_client_id,
                "redirect_uri": settings.kakao_redirect_uri,
                "code": authorization_code,
            },
        )
        response.raise_for_status()
        data = response.json()
        return KakaoTokenInfo(
            access_token=data["access_token"],
            refresh_token=data.get("refresh_token", ""),
            expires_in=data.get("expires_in", 0),
        )

    def get_kakao_user_info(self, kakao_access_token: str) -> KakaoUserInfo:
        response = httpx.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {kakao_access_token}"},
        )
        response.raise_for_status()
        data = response.json()
        kakao_account = data.get("kakao_account", {})
        return KakaoUserInfo(
            kakao_id=str(data["id"]),
            name=kakao_account.get("profile", {}).get("nickname", ""),
            email=kakao_account.get("email", ""),
        )

    def get_oauth_url(self) -> str:
        params = urlencode({
            "client_id": settings.kakao_client_id,
            "redirect_uri": settings.kakao_redirect_uri,
            "response_type": "code",
        })
        return f"https://kauth.kakao.com/oauth/authorize?{params}"
