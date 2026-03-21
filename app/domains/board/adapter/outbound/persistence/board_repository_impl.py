from sqlalchemy.orm import Session

from app.domains.board.adapter.outbound.persistence.board_repository import BoardRepository
from app.domains.board.domain.entity.board import Board
from app.domains.board.infrastructure.mapper.board_mapper import BoardMapper


class BoardRepositoryImpl(BoardRepository):
    def __init__(self, db: Session):
        self.db = db

    def save(self, board: Board) -> Board:
        orm = BoardMapper.to_orm(board)
        self.db.add(orm)
        self.db.commit()
        self.db.refresh(orm)
        return BoardMapper.to_entity(orm)
