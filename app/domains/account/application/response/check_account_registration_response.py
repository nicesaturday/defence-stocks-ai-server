from typing import Optional

from pydantic import BaseModel


class CheckAccountRegistrationResponse(BaseModel):
    is_registered: bool
    account_id: Optional[int] = None
