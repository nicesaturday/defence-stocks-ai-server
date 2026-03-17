import redis

from app.infrastructure.config.settings import settings

redis_client = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    db=settings.redis_db,
    password=settings.redis_password,
    decode_responses=True,
)


def get_redis() -> redis.Redis:
    return redis_client
