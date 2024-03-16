from django.contrib.auth.middleware import get_user
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class TokenAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # Extract token from cookies
            token_key = request.COOKIES.get('auth_token')
            if token_key:
                user, token = TokenAuthentication().authenticate_credentials(token_key)
                request.user = user
        except AuthenticationFailed:
            pass

        response = self.get_response(request)
        return response