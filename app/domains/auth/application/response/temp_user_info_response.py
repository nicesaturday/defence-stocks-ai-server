from typing import Optional

from pydantic import BaseModel


class TempUserInfoResponse(BaseModel):
    is_registered: bool
    nickname: str
    email: str
    account_id: Optional[int] = None
