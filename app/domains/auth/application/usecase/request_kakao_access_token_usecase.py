import logging

from app.domains.account.application.usecase.check_account_registration_usecase import CheckAccountRegistrationUseCase
from app.domains.auth.adapter.outbound.external.kakao_auth_port import KakaoAuthPort
from app.domains.auth.application.response.kakao_access_token_response import KakaoAccessTokenResponse

logger = logging.getLogger(__name__)


class RequestKakaoAccessTokenUseCase:
    def __init__(
        self,
        kakao_auth_port: KakaoAuthPort,
        check_account_registration_usecase: CheckAccountRegistrationUseCase,
    ):
        self.kakao_auth_port = kakao_auth_port
        self.check_account_registration_usecase = check_account_registration_usecase

    def execute(self, authorization_code: str) -> KakaoAccessTokenResponse:
        token_info = self.kakao_auth_port.get_kakao_access_token(authorization_code)
        user_info = self.kakao_auth_port.get_kakao_user_info(token_info.access_token)

        logger.info("Kakao 사용자 정보 - 닉네임: %s, 이메일: %s", user_info.name, user_info.email)

        registration = self.check_account_registration_usecase.execute(user_info.email)

        return KakaoAccessTokenResponse(
            access_token=token_info.access_token,
            refresh_token=token_info.refresh_token,
            expires_in=token_info.expires_in,
            kakao_id=user_info.kakao_id,
            nickname=user_info.name,
            email=user_info.email,
            is_registered=registration.is_registered,
            account_id=registration.account_id,
        )
