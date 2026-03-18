from fastapi import APIRouter, Depends

from app.domains.auth.application.request.kakao_login_request import KakaoLoginRequest
from app.domains.auth.application.response.kakao_login_response import KakaoLoginResponse
from app.domains.auth.application.usecase.kakao_login_usecase import KakaoLoginUseCase
from app.domains.auth.dependency import get_kakao_login_usecase

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/kakao", response_model=KakaoLoginResponse)
def kakao_login(
    request: KakaoLoginRequest,
    usecase: KakaoLoginUseCase = Depends(get_kakao_login_usecase),
):
    return usecase.execute(request)
