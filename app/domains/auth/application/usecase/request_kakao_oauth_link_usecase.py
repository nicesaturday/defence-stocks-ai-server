from app.domains.auth.adapter.outbound.external.kakao_auth_port import KakaoAuthPort
from app.domains.auth.application.response.kakao_oauth_url_response import KakaoOauthUrlResponse


class RequestKakaoOauthLinkUseCase:
    def __init__(self, kakao_auth_port: KakaoAuthPort):
        self.kakao_auth_port = kakao_auth_port

    def execute(self) -> KakaoOauthUrlResponse:
        oauth_url = self.kakao_auth_port.get_oauth_url()
        return KakaoOauthUrlResponse(oauth_url=oauth_url)
