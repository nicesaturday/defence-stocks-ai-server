from app.domains.board.adapter.outbound.persistence.board_repository import BoardRepository
from app.domains.board.application.request.create_board_request import CreateBoardRequest
from app.domains.board.application.response.create_board_response import CreateBoardResponse
from app.domains.board.domain.entity.board import Board


class CreateBoardUseCase:
    def __init__(self, board_repository: BoardRepository):
        self.board_repository = board_repository

    def execute(self, request: CreateBoardRequest, account_id: int) -> CreateBoardResponse:
        board = Board(
            title=request.title,
            content=request.content,
            account_id=account_id,
        )
        board.validate()
        board = self.board_repository.save(board)

        return CreateBoardResponse(
            board_id=board.board_id,
            title=board.title,
            content=board.content,
            account_id=board.account_id,
            created_at=board.created_at,
            updated_at=board.updated_at,
        )
