from fastapi import APIRouter

from app.domains.auth.adapter.outbound.external.kakao_auth_client import KakaoAuthClient
from app.domains.auth.application.response.kakao_oauth_url_response import KakaoOauthUrlResponse
from app.domains.auth.application.usecase.request_kakao_oauth_link_usecase import RequestKakaoOauthLinkUseCase

router = APIRouter(prefix="/kakao-authentication", tags=["Kakao Authentication"])


@router.get("/request-oauth-link", response_model=KakaoOauthUrlResponse)
def request_oauth_link():
    kakao_client = KakaoAuthClient()
    usecase = RequestKakaoOauthLinkUseCase(kakao_client)
    return usecase.execute()
