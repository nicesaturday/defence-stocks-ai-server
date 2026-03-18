from fastapi import Depends
from sqlalchemy.orm import Session

from app.domains.account.adapter.outbound.persistence.account_repository import AccountRepository
from app.domains.account.adapter.outbound.persistence.account_repository_impl import AccountRepositoryImpl
from app.domains.account.application.usecase.check_account_registration_usecase import CheckAccountRegistrationUseCase
from app.infrastructure.database.session import get_db


def get_account_repository(db: Session = Depends(get_db)) -> AccountRepository:
    return AccountRepositoryImpl(db)


def get_check_account_registration_usecase(
    account_repository: AccountRepository = Depends(get_account_repository),
) -> CheckAccountRegistrationUseCase:
    return CheckAccountRegistrationUseCase(account_repository)
