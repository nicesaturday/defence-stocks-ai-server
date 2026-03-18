from app.domains.account.adapter.outbound.persistence.account_repository import AccountRepository
from app.domains.account.application.response.check_account_registration_response import CheckAccountRegistrationResponse


class CheckAccountRegistrationUseCase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def execute(self, email: str) -> CheckAccountRegistrationResponse:
        account = self.account_repository.find_by_email(email)

        if account is None:
            return CheckAccountRegistrationResponse(is_registered=False)

        return CheckAccountRegistrationResponse(
            is_registered=True,
            account_id=account.account_id,
        )
