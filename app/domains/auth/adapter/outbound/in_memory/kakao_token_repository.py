from abc import ABC, abstractmethod


class KakaoTokenRepository(ABC):
    @abstractmethod
    def save(self, account_id: int, kakao_access_token: str) -> None:
        pass
