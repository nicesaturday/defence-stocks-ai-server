from typing import Optional

from app.domains.account.adapter.outbound.persistence.account_repository import AccountRepository
from app.domains.auth.adapter.outbound.in_memory.session_repository import SessionRepository
from app.domains.auth.adapter.outbound.in_memory.temp_token_repository import TempTokenRepository
from app.domains.auth.application.response.temp_user_info_response import TempUserInfoResponse


class GetTempUserInfoUseCase:
    def __init__(
        self,
        temp_token_repository: TempTokenRepository,
        session_repository: SessionRepository,
        account_repository: AccountRepository,
    ):
        self.temp_token_repository = temp_token_repository
        self.session_repository = session_repository
        self.account_repository = account_repository

    def execute(
        self,
        temp_token: Optional[str] = None,
        user_token: Optional[str] = None,
    ) -> TempUserInfoResponse:
        if user_token:
            return self._handle_user_token(user_token)

        if temp_token:
            return self._handle_temp_token(temp_token)

        raise ValueError("토큰이 존재하지 않습니다.")

    def _handle_user_token(self, user_token: str) -> TempUserInfoResponse:
        print(f"기존 회원 정보 조회 - user_token: {user_token[:8]}...")

        account_id = self.session_repository.find_by_token(user_token)
        if account_id is None:
            print(f"세션 조회 실패 - user_token: {user_token[:8]}...")
            raise ValueError("세션이 만료되었거나 존재하지 않습니다.")

        account = self.account_repository.find_by_id(account_id)
        if account is None:
            raise ValueError("회원 정보를 찾을 수 없습니다.")

        print(f"기존 회원 정보 조회 성공 - nickname: {account.name}, email: {account.email}, account_id: {account.account_id}")

        return TempUserInfoResponse(
            is_registered=True,
            nickname=account.name,
            email=account.email,
            account_id=account.account_id,
        )

    def _handle_temp_token(self, temp_token: str) -> TempUserInfoResponse:
        print(f"임시 사용자 정보 조회 - temp_token: {temp_token[:8]}...")

        temp_data = self.temp_token_repository.find_by_token(temp_token)
        if temp_data is None:
            print(f"임시 토큰 조회 실패 - temp_token: {temp_token[:8]}...")
            raise ValueError("임시 토큰이 만료되었거나 존재하지 않습니다.")

        print(f"임시 사용자 정보 조회 성공 - nickname: {temp_data['nickname']}, email: {temp_data['email']}")

        return TempUserInfoResponse(
            is_registered=False,
            nickname=temp_data["nickname"],
            email=temp_data["email"],
        )
