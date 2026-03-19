import redis

from app.domains.auth.adapter.outbound.in_memory.kakao_token_repository import KakaoTokenRepository
from app.infrastructure.config.settings import settings


class KakaoTokenRepositoryImpl(KakaoTokenRepository):
    def __init__(self, redis_client: redis.Redis):
        self.redis_client = redis_client

    def save(self, account_id: int, kakao_access_token: str) -> None:
        key = f"kakao_token:{account_id}"
        self.redis_client.setex(
            key,
            settings.session_expire_minutes * 60,
            kakao_access_token,
        )
