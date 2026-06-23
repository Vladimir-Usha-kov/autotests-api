from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

class Exercise(TypedDict):
    """Структура курса"""
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesResponseDict(TypedDict):
    """Описание структуры ответа на запрос всех заданий у курса"""
    exercises: list[Exercise]


class CreateExercisesResponseDict(TypedDict):
    """Описание структуры ответа на создание курса"""
    exercise: Exercise


class GetExerciseResponseDict(TypedDict):
    """Описание структуры ответа на определенное задание"""
    exercise: Exercise


class UpdateExerciseResponseDict(TypedDict):
    """Описание структуры ответа по обновленным полям"""
    exercise: Exercise


class QueryExercisesDict(TypedDict):
    """Словарь для айди курса"""
    courseId: str


class CreateExercisesRequestDict(TypedDict):
    """Словарь для создания задания"""
    title: str
    courseId: str
    maxScore: int
    minScore:int
    orderIndex:int
    description: str
    estimatedTime: str


class UpdateExercisesRequestDict(TypedDict):
    """Словарь для обновления задания"""
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """Клиент для /api/v1/exercises"""

    def get_exercises_api(self, query: QueryExercisesDict) -> Response:
        """
        Метод для получение списка заданий для определенного курса.
        :param query: Словарь с ключом courseId
        :return: Возвращает ответ вида httpx.Response
        """
        return self.get(url='/api/v1/exercises', params=query)


    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для получение задания по id
        :param exercise_id: Идентификатор задания
        :return: Возвращает ответ вида httpx.Response
        """
        return self.get(url=f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод для создания задания
        :param request: Словарь с ключами title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Возвращает ответ вида httpx.Response
        """
        return self.post(url='/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Метод для обновление задания
        :param exercise_id: Идентификатор задания
        :param request: Словарь с ключами title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Возвращает ответ вида httpx.Response
        """
        return self.patch(url=f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаление задания
        :param exercise_id: Идентификатор задания
        :return: Возвращает ответ вида httpx.Response
        """
        return self.delete(url=f'/api/v1/exercises/{exercise_id}')

    def get_exercises(self, query: QueryExercisesDict) -> GetExercisesResponseDict:
        """
        Метод для запроса задания по courseId через query
        :param query: Словарь с ключом courseId
        :return: Возвращает в овтете задания
        """
        response = self.get_exercises_api(query)
        return response.json()


    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод для запроса определенного задания
        :param exercise_id: id задания
        :return: Возвращает ответ по запрашиваемоу заданию
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExercisesRequestDict) -> CreateExercisesResponseDict:
        """
        Метод создания курса
        :param request: Словарь с ключами title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Возвращает ответ с информацией о созданном задании
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод обновляет задание
        :param exercise_id: id задания
        :param request: Поля кльлоые хотим изменить
        :return: Возвращает измененное задание
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return response.json()

def get_exercise_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
   Функция создает экземпляпр ExercisesClient с уже настроенным HTTP-клиентом
   :return: Готовый к использованию ExercisesClient
   """
    return ExercisesClient(get_private_http_client(user))