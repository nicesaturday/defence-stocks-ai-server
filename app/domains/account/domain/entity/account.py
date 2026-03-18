from datetime import datetime
from typing import Optional


class Account:
    def __init__(
        self,
        email: str,
        account_id: Optional[int] = None,
        kakao_id: Optional[str] = None,
        name: Optional[str] = None,
        created_at: Optional[datetime] = None,
    ):
        self.account_id = account_id
        self.email = email
        self.kakao_id = kakao_id
        self.name = name
        self.created_at = created_at or datetime.now()
