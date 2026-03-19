import json
from typing import Optional

import redis

from app.domains.auth.adapter.outbound.in_memory.session_repository import SessionRepository
from app.infrastructure.config.settings import settings


class SessionRepositoryImpl(SessionRepository):
    def __init__(self, redis_client: redis.Redis):
        self.redis_client = redis_client

    def _key(self, token: str) -> str:
        return f"session:{token}"

    def save(self, token: str, account_id: int, kakao_access_token: str) -> None:
        data = json.dumps({"account_id": account_id, "kakao_access_token": kakao_access_token})
        self.redis_client.setex(
            self._key(token),
            settings.session_expire_minutes * 60,
            data,
        )

    def find_by_token(self, token: str) -> Optional[dict]:
        data = self.redis_client.get(self._key(token))
        if data is None:
            return None
        return json.loads(data)

    def delete_by_token(self, token: str) -> None:
        self.redis_client.delete(self._key(token))
