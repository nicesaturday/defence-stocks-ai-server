from abc import ABC, abstractmethod


class TempTokenRepository(ABC):
    @abstractmethod
    def save(self, token: str, nickname: str, email: str) -> None:
        pass
