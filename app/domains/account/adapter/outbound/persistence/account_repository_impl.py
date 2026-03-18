from typing import Optional

from sqlalchemy.orm import Session

from app.domains.account.adapter.outbound.persistence.account_repository import AccountRepository
from app.domains.account.domain.entity.account import Account
from app.domains.account.infrastructure.mapper.account_mapper import AccountMapper
from app.domains.account.infrastructure.orm.account_orm import AccountORM


class AccountRepositoryImpl(AccountRepository):
    def __init__(self, db: Session):
        self.db = db

    def find_by_email(self, email: str) -> Optional[Account]:
        orm = self.db.query(AccountORM).filter(AccountORM.email == email).first()
        if orm is None:
            return None
        return AccountMapper.to_entity(orm)
