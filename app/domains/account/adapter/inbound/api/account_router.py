from fastapi import APIRouter, Cookie, Depends, HTTPException
from starlette.responses import JSONResponse

from app.domains.auth.application.request.sign_up_request import SignUpRequest
from app.domains.auth.application.response.sign_up_response import SignUpResponse
from app.domains.auth.application.usecase.sign_up_with_temp_token_usecase import SignUpWithTempTokenUseCase
from app.domains.auth.dependency import get_sign_up_with_temp_token_usecase

router = APIRouter(prefix="/account", tags=["Account"])


@router.post("/sign-up", response_model=SignUpResponse)
def sign_up(
    request: SignUpRequest,
    temp_token: str = Cookie(None),
    usecase: SignUpWithTempTokenUseCase = Depends(get_sign_up_with_temp_token_usecase),
):
    if not temp_token:
        raise HTTPException(status_code=400, detail="임시 토큰이 누락되었습니다.")

    try:
        result, user_token = usecase.execute(temp_token, request)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

    response = JSONResponse(content=result.model_dump())
    response.set_cookie(
        key="user_token",
        value=user_token,
        httponly=True,
        samesite="lax",
    )
    response.delete_cookie(key="temp_token")
    return response
