from typing import Optional

from fastapi import APIRouter, Cookie, Depends, HTTPException, Query

from app.domains.auth.adapter.outbound.in_memory.session_repository import SessionRepository
from app.domains.youtube.application.response.youtube_list_response import YoutubeListResponse
from app.domains.youtube.application.usecase.list_youtube_usecase import ListYoutubeUseCase
from app.domains.youtube.dependency import get_list_youtube_usecase, get_session_repository

router = APIRouter(prefix="/youtube", tags=["YouTube"])


@router.get("/list", response_model=YoutubeListResponse)
def list_youtube_videos(
    page_token: Optional[str] = Query(None),
    user_token: str = Cookie(None),
    usecase: ListYoutubeUseCase = Depends(get_list_youtube_usecase),
    session_repository: SessionRepository = Depends(get_session_repository),
):
    if not user_token:
        raise HTTPException(status_code=401, detail="인증이 필요합니다.")

    account_id = session_repository.find_by_token(user_token)
    if account_id is None:
        raise HTTPException(status_code=401, detail="세션이 만료되었거나 유효하지 않습니다.")

    return usecase.execute(page_token)
