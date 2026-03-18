from app.domains.account.domain.entity.account import Account
from app.domains.account.infrastructure.orm.account_orm import AccountORM


class AccountMapper:
    @staticmethod
    def to_entity(orm: AccountORM) -> Account:
        return Account(
            account_id=orm.id,
            email=orm.email,
            kakao_id=orm.kakao_id,
            name=orm.name,
            created_at=orm.created_at,
        )
