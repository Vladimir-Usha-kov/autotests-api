from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class QueryExercisesDict(TypedDict):
    """Словарь для айди курса"""
    courseId: str


class CreateExercisesDict(TypedDict):
    """Словарь для создания задания"""
    title: str
    courseId: str
    maxScore: int
    minScore:int
    orderIndex:int
    description: str
    estimatedTime: str


class UpdateExercisesDict(TypedDict):
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

    def create_exercise_api(self, request: CreateExercisesDict) -> Response:
        """
        Метод для создания задания
        :param request: Словарь с ключами title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Возвращает ответ вида httpx.Response
        """
        return self.post(url='/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesDict) -> Response:
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