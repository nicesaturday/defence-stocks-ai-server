from app.domains.auth.adapter.outbound.external.kakao_auth_port import KakaoAuthPort
from app.domains.auth.application.response.kakao_access_token_response import KakaoAccessTokenResponse


class RequestKakaoAccessTokenUseCase:
    def __init__(self, kakao_auth_port: KakaoAuthPort):
        self.kakao_auth_port = kakao_auth_port

    def execute(self, authorization_code: str) -> KakaoAccessTokenResponse:
        token_info = self.kakao_auth_port.get_kakao_access_token(authorization_code)
        return KakaoAccessTokenResponse(
            access_token=token_info.access_token,
            refresh_token=token_info.refresh_token,
            expires_in=token_info.expires_in,
        )
