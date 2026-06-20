from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response

from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class QueryParamsDict(TypedDict):
    userId: str


class CreateCourseDict(TypedDict):
    title: str
    maxScor: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId:str


class UpdateCourseDict(TypedDict):
    title: str | None
    maxScor: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    """Клиент для работы с /api/v1/courses"""

    def get_courses_api(self, request: QueryParamsDict) -> Response:
        """
        Метод для получение списка курсов для определенного пользователя.
        :param request: Словарь с ключом userId
        :return: Возвращает ответ вида httpx.Response
        """
        return self.get(url='/api/v1/courses', params=request)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод для получение курса по идентификартору
        :param course_id: Идентификатора курса
        :return: Возвращает ответ вида httpx.Response
        """
        return self.get(url=f'/api/v1/courses/{course_id}')

    def create_course_api(self, request: CreateCourseDict) -> Response:
        """
        Метод для создание курса
        :param request: Словарь с ключами title, maxScor, minScore, description, estimatedTime,
        previewFileId, createdByUserId
        :return: Возвращает ответ вида httpx.Response
        """
        return self.post(url='/api/v1/courses', json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseDict) -> Response:
        """
        Метод для обновление курса по идентификартору
        :param course_id: Идентификатора курса
        :param request: Словарь с ключами title, maxScor, minScore, description, estimatedTime
        :return: Возвращает ответ вида httpx.Response
        """
        return self.patch(url=f'/api/v1/courses/{course_id}', json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод для удаление курса по идентификатору
        :param course_id: Идентификатор курса
        :return: Возвращает ответ вида httpx.Response
        """
        return self.delete(url=f'/api/v1/courses/{course_id}')


def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Функция создает экземпляпр CoursesClient с уже настроенным HTTP-клиентом
    :return: Готовый к использованию CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user))