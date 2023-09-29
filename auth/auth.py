from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from config import BACKEND_AUTH_SECRET_KEY

cookie_transport = CookieTransport(cookie_max_age=3600, cookie_name="mylib-auth-cookie")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=BACKEND_AUTH_SECRET_KEY, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy
)