import allure

from clients.api_client import APIClient
from httpx import Response
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema
from tools.routes import ApiRoutes


class PrivateUsersClient(APIClient):
    """Клиент для работы с /api/v1/users"""

    @allure.step('GET user me')
    def get_user_me_api(self) -> Response:
        """
        Метод поулчения текущего пользователя

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'{ApiRoutes.USERS}/me')

    @allure.step('GET user by id: {user_id}')
    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получение пользователя по айди

        :param user_id: Индификатор пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'{ApiRoutes.USERS}/{user_id}')

    @allure.step('Update user by id: {user_id}')
    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод частичного обновления данных пользователя

        :param user_id: Индификатор пользователя
        :param request: Словарь с email, lastName, firstName, middleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f'{ApiRoutes.USERS}/{user_id}', json=request.model_dump(by_alias=True))

    @allure.step('Delete user by id: {user_id}')
    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по айди

        :param user_id: Индификатор пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'{ApiRoutes.USERS}/{user_id}')

    def get_user(self, user_id: str ) -> GetUserResponseSchema:
        response = self.get_user_api(user_id=user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создает экзепляр PrivateUsersClient с уже настроенным HTTP-клиентом
    :return: Готовый к использованию PrivateUsersClient
    """
    return PrivateUsersClient(client=get_private_http_client(user))




