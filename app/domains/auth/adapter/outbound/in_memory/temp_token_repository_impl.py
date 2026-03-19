import json

import redis

from app.domains.auth.adapter.outbound.in_memory.temp_token_repository import TempTokenRepository

TEMP_TOKEN_TTL_SECONDS = 5 * 60


class TempTokenRepositoryImpl(TempTokenRepository):
    def __init__(self, redis_client: redis.Redis):
        self.redis_client = redis_client

    def save(self, token: str, nickname: str, email: str) -> None:
        key = f"temp_token:{token}"
        data = json.dumps({"nickname": nickname, "email": email})
        self.redis_client.setex(key, TEMP_TOKEN_TTL_SECONDS, data)
