
from httpx import Client
from typing import TypedDict

from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict, \
    AuthenticationClient


class AuthenticationUserDict(TypedDict):
    email: str
    password: str

def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
       Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

       :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
       :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
       """
    authentication_client = get_authentication_client()
    login_request = LoginRequestDict(email=user["email"], password=user["password"])
    login_response = authentication_client.login(request=login_request)

    return Client(
        base_url='http://localhost:8000',
        timeout=100,
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )

