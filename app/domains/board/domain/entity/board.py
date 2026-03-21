from datetime import datetime
from typing import Optional


class Board:
    def __init__(
        self,
        title: str,
        content: str,
        account_id: int,
        board_id: Optional[int] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.board_id = board_id
        self.title = title
        self.content = content
        self.account_id = account_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def validate(self) -> None:
        if not self.title or not self.title.strip():
            raise ValueError("게시물 제목은 비어 있을 수 없습니다.")
        if not self.content or not self.content.strip():
            raise ValueError("게시물 내용은 비어 있을 수 없습니다.")
