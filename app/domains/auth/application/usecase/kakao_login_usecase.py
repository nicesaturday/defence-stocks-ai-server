from app.domains.account.adapter.outbound.persistence.account_repository import AccountRepository
from app.domains.account.domain.entity.account import Account
from app.domains.auth.adapter.outbound.external.kakao_auth_port import KakaoAuthPort
from app.domains.auth.application.request.kakao_login_request import KakaoLoginRequest
from app.domains.auth.application.response.kakao_login_response import KakaoLoginResponse
from app.infrastructure.security.jwt_provider import JwtProvider


class KakaoLoginUseCase:
    def __init__(
        self,
        account_repository: AccountRepository,
        kakao_auth_port: KakaoAuthPort,
        jwt_provider: JwtProvider,
    ):
        self.account_repository = account_repository
        self.kakao_auth_port = kakao_auth_port
        self.jwt_provider = jwt_provider

    def execute(self, request: KakaoLoginRequest) -> KakaoLoginResponse:
        token_info = self.kakao_auth_port.get_kakao_access_token(request.authorization_code)
        user_info = self.kakao_auth_port.get_kakao_user_info(token_info.access_token)

        account = self.account_repository.find_by_kakao_id(user_info.kakao_id)
        if account is None:
            account = Account(
                kakao_id=user_info.kakao_id,
                name=user_info.name,
                email=user_info.email,
            )
            account = self.account_repository.save(account)

        access_token = self.jwt_provider.generate_token(account.account_id)
        return KakaoLoginResponse(access_token=access_token)
