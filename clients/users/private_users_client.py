from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class RequestUpdateUserApiDict(TypedDict):
    """Описание структуры запроса на обновление пользователя"""

    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivateUsersClient(APIClient):
    """Клиент для работы с /api/v1/users"""

    def get_user_me_api(self) -> Response:
        """
        Метод поулчения текущего пользователя

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url='/api/v1/users/me')



    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получение пользователя по айди

        :param user_id: Индификатор пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'/api/v1/users/{user_id}')


    def update_user_api(self, user_id: str, request: RequestUpdateUserApiDict) -> Response:
        """
        Метод частичного обновления данных пользователя

        :param user_id: Индификатор пользователя
        :param request: Словарь с email, lastName, firstName, middleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f'/api/v1/users/{user_id}', json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по айди

        :param user_id: Индификатор пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'/api/v1/users/{user_id}')


def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    """
    Функция создает экзепляр PrivateUsersClient с уже настроенным HTTP-клиентом
    :return: Готовый к использованию PrivateUsersClient
    """
    return PrivateUsersClient(client=get_private_http_client(user))




