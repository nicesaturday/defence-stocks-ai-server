from fastapi import Depends

from app.domains.auth.adapter.outbound.in_memory.session_repository import SessionRepository
from app.domains.auth.adapter.outbound.in_memory.session_repository_impl import SessionRepositoryImpl
from app.domains.youtube.adapter.outbound.external.youtube_client import YoutubeClient
from app.domains.youtube.adapter.outbound.external.youtube_port import YoutubePort
from app.domains.youtube.application.usecase.list_youtube_usecase import ListYoutubeUseCase
from app.infrastructure.cache.redis_client import get_redis


def get_session_repository() -> SessionRepository:
    return SessionRepositoryImpl(get_redis())


def get_youtube_port() -> YoutubePort:
    return YoutubeClient()


def get_list_youtube_usecase(
    youtube_port: YoutubePort = Depends(get_youtube_port),
) -> ListYoutubeUseCase:
    return ListYoutubeUseCase(youtube_port)
