from typing import Optional

import redis

from app.domains.auth.adapter.outbound.in_memory.session_repository import SessionRepository
from app.infrastructure.config.settings import settings


class SessionRepositoryImpl(SessionRepository):
    def __init__(self, redis_client: redis.Redis):
        self.redis_client = redis_client

    def _key(self, token: str) -> str:
        return f"session:{token}"

    def save(self, token: str, account_id: int) -> None:
        self.redis_client.setex(
            self._key(token),
            settings.session_expire_minutes * 60,
            str(account_id),
        )

    def find_by_token(self, token: str) -> Optional[int]:
        data = self.redis_client.get(self._key(token))
        if data is None:
            return None
        return int(data)

    def delete_by_token(self, token: str) -> None:
        self.redis_client.delete(self._key(token))
