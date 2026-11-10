import allure

from clients.api_client import APIClient
from httpx import Response
from clients.courses.course_schema import GetCoursesQuerySchema, CreateCourseRequestSchema, CreateCourseResponseSchema, \
    UpdateCourseRequestSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from tools.routes import ApiRoutes


class CoursesClient(APIClient):
    """Клиент для работы с /api/v1/courses"""

    @allure.step('Get courses')
    def get_courses_api(self, request: GetCoursesQuerySchema) -> Response:
        """
        Метод для получение списка курсов для определенного пользователя.
        :param request: Словарь с ключом userId
        :return: Возвращает ответ вида httpx.Response
        """
        return self.get(url=ApiRoutes.COURSES, params=request.model_dump(by_alias=True))

    @allure.step('Get course by id: {course_id}')
    def get_course_api(self, course_id: str) -> Response:
        """
        Метод для получение курса по идентификартору
        :param course_id: Идентификатора курса
        :return: Возвращает ответ вида httpx.Response
        """
        return self.get(url=f'{ApiRoutes.COURSES}/{course_id}')

    @allure.step('Create courses')
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод для создание курса
        :param request: Словарь с ключами title, maxScor, minScore, description, estimatedTime,
        previewFileId, createdByUserId
        :return: Возвращает ответ вида httpx.Response
        """
        return self.post(url=ApiRoutes.COURSES, json=request.model_dump(by_alias=True))

    @allure.step('Update courses by id: {course_id}')
    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод для обновление курса по идентификартору
        :param course_id: Идентификатора курса
        :param request: Словарь с ключами title, maxScor, minScore, description, estimatedTime
        :return: Возвращает ответ вида httpx.Response
        """
        return self.patch(url=f'{ApiRoutes.COURSES}/{course_id}', json=request.model_dump(by_alias=True))

    @allure.step('Delete courses by id: {course_id}')
    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод для удаление курса по идентификатору
        :param course_id: Идентификатор курса
        :return: Возвращает ответ вида httpx.Response
        """
        return self.delete(url=f'{ApiRoutes.COURSES}/{course_id}')

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request=request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создает экземпляпр CoursesClient с уже настроенным HTTP-клиентом
    :return: Готовый к использованию CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user))
