import allure

from clients.api_client import APIClient
from httpx import Response

from clients.exercises.exercises_schema import QueryExercisesSchema, CreateExerciseRequestSchema, \
    UpdateExercisesRequestSchema, GetExercisesResponseSchema, CreateExercisesResponseSchema, \
    UpdateExerciseResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from tools.routes import ApiRoutes


class ExercisesClient(APIClient):
    """Клиент для /api/v1/exercises"""
    @allure.step('GET exercises')
    def get_exercises_api(self, query: QueryExercisesSchema) -> Response:
        """
        Метод для получение списка заданий для определенного курса.
        :param query: Словарь с ключом courseId
        :return: Возвращает ответ вида httpx.Response
        """
        return self.get(url=ApiRoutes.EXERCISES, params=query.model_dump(by_alias=True))

    @allure.step('GET exercises by id: {exercise_id}')
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для получение задания по id
        :param exercise_id: Идентификатор задания
        :return: Возвращает ответ вида httpx.Response
        """
        return self.get(url=f'{ApiRoutes.EXERCISES}/{exercise_id}')

    @allure.step('Create exercises')
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод для создания задания
        :param request: Словарь с ключами title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Возвращает ответ вида httpx.Response
        """
        return self.post(url=ApiRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    @allure.step('Update exercises by id: {exercise_id}')
    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestSchema) -> Response:
        """
        Метод для обновление задания
        :param exercise_id: Идентификатор задания
        :param request: Словарь с ключами title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Возвращает ответ вида httpx.Response
        """
        return self.patch(
            url=f'{ApiRoutes.EXERCISES}/{exercise_id}',
            json=request.model_dump(by_alias=True)
        )

    @allure.step('Delete exercises by id: {exercise_id}')
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаление задания
        :param exercise_id: Идентификатор задания
        :return: Возвращает ответ вида httpx.Response
        """
        return self.delete(url=f'{ApiRoutes.EXERCISES}/{exercise_id}')

    def get_exercises(self, query: QueryExercisesSchema) -> GetExercisesResponseSchema:
        """
        Метод для запроса задания по courseId через query
        :param query: Словарь с ключом courseId
        :return: Возвращает в овтете задания
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExercisesResponseSchema:
        """
        Метод для запроса определенного задания
        :param exercise_id: id задания
        :return: Возвращает ответ по запрашиваемоу заданию
        """
        response = self.get_exercise_api(exercise_id)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExercisesResponseSchema:
        """
        Метод создания курса
        :param request: Словарь с ключами title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Возвращает ответ с информацией о созданном задании
        """
        response = self.create_exercise_api(request)
        return CreateExercisesResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Метод обновляет задание
        :param exercise_id: id задания
        :param request: Поля кльлоые хотим изменить
        :return: Возвращает измененное задание
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
   Функция создает экземпляпр ExercisesClient с уже настроенным HTTP-клиентом
   :return: Готовый к использованию ExercisesClient
   """
    return ExercisesClient(get_private_http_client(user))
