from app.domains.auth.adapter.outbound.external.kakao_auth_port import KakaoAuthPort


class RequestKakaoOauthLinkUseCase:
    def __init__(self, kakao_auth_port: KakaoAuthPort):
        self.kakao_auth_port = kakao_auth_port

    def execute(self) -> str:
        return self.kakao_auth_port.get_oauth_url()
