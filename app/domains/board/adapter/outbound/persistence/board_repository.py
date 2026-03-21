from abc import ABC, abstractmethod

from app.domains.board.domain.entity.board import Board


class BoardRepository(ABC):
    @abstractmethod
    def save(self, board: Board) -> Board:
        pass
