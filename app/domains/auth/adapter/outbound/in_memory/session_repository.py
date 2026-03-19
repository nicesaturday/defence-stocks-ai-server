from abc import ABC, abstractmethod
from typing import Optional


class SessionRepository(ABC):
    @abstractmethod
    def save(self, token: str, account_id: int) -> None:
        pass

    @abstractmethod
    def find_by_token(self, token: str) -> Optional[int]:
        pass

    @abstractmethod
    def delete_by_token(self, token: str) -> None:
        pass
