from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateBoardResponse(BaseModel):
    board_id: Optional[int]
    title: str
    content: str
    account_id: int
    created_at: datetime
    updated_at: datetime
