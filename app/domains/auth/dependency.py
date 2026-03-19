from fastapi import Depends
from sqlalchemy.orm import Session

from app.domains.account.adapter.outbound.persistence.account_repository import AccountRepository
from app.domains.account.application.usecase.check_account_registration_usecase import CheckAccountRegistrationUseCase
from app.domains.account.dependency import get_account_repository, get_check_account_registration_usecase
from app.domains.auth.adapter.outbound.external.kakao_auth_client import KakaoAuthClient
from app.domains.auth.adapter.outbound.external.kakao_auth_port import KakaoAuthPort
from app.domains.auth.application.usecase.kakao_login_usecase import KakaoLoginUseCase
from app.domains.auth.application.usecase.request_kakao_access_token_usecase import RequestKakaoAccessTokenUseCase
from app.domains.auth.application.usecase.request_kakao_oauth_link_usecase import RequestKakaoOauthLinkUseCase
from app.infrastructure.security.jwt_provider import JwtProvider


def get_kakao_auth_port() -> KakaoAuthPort:
    return KakaoAuthClient()


def get_jwt_provider() -> JwtProvider:
    return JwtProvider()


def get_kakao_login_usecase(
    account_repository: AccountRepository = Depends(get_account_repository),
    kakao_auth_port: KakaoAuthPort = Depends(get_kakao_auth_port),
    jwt_provider: JwtProvider = Depends(get_jwt_provider),
) -> KakaoLoginUseCase:
    return KakaoLoginUseCase(account_repository, kakao_auth_port, jwt_provider)


def get_request_kakao_oauth_link_usecase(
    kakao_auth_port: KakaoAuthPort = Depends(get_kakao_auth_port),
) -> RequestKakaoOauthLinkUseCase:
    return RequestKakaoOauthLinkUseCase(kakao_auth_port)


def get_request_kakao_access_token_usecase(
    kakao_auth_port: KakaoAuthPort = Depends(get_kakao_auth_port),
    check_account_registration_usecase: CheckAccountRegistrationUseCase = Depends(get_check_account_registration_usecase),
) -> RequestKakaoAccessTokenUseCase:
    return RequestKakaoAccessTokenUseCase(kakao_auth_port, check_account_registration_usecase)
