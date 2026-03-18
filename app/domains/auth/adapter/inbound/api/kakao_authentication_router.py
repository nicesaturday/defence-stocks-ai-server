from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import RedirectResponse

from app.domains.auth.application.response.kakao_access_token_response import KakaoAccessTokenResponse
from app.domains.auth.application.usecase.request_kakao_access_token_usecase import RequestKakaoAccessTokenUseCase
from app.domains.auth.application.usecase.request_kakao_oauth_link_usecase import RequestKakaoOauthLinkUseCase
from app.domains.auth.dependency import get_request_kakao_access_token_usecase, get_request_kakao_oauth_link_usecase

router = APIRouter(prefix="/kakao-authentication", tags=["Kakao Authentication"])


@router.get("/request-oauth-link")
def request_oauth_link(
    usecase: RequestKakaoOauthLinkUseCase = Depends(get_request_kakao_oauth_link_usecase),
):
    oauth_url = usecase.execute()
    return RedirectResponse(url=oauth_url)


@router.get("/request-access-token-after-redirection", response_model=KakaoAccessTokenResponse)
def request_access_token_after_redirection(
    code: str,
    usecase: RequestKakaoAccessTokenUseCase = Depends(get_request_kakao_access_token_usecase),
):
    if not code:
        raise HTTPException(status_code=400, detail="인가 코드가 누락되었습니다.")
    return usecase.execute(code)
