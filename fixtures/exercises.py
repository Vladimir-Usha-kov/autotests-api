import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import get_exercise_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExercisesResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.user import UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExercisesResponseSchema

    @property
    def exercise_id(self) -> str:
        return self.response.exercise.id


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercise_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(exercises_client: ExercisesClient, function_course: CoursesFixture) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(course_id=function_course.course_id)
    response = exercises_client.create_exercise(request)

    return ExerciseFixture(request=request, response=response)
