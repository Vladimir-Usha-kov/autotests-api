from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake


class ExerciseSchema(BaseModel):
    """Структура курса"""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class GetExercisesResponseSchema(BaseModel):
    """Описание структуры ответа на запрос всех заданий у курса"""
    exercises: list[ExerciseSchema]


class CreateExercisesResponseSchema(BaseModel):
    """Описание структуры ответа на создание курса"""
    exercise: ExerciseSchema


class GetExerciseResponseSchema(BaseModel):
    """Описание структуры ответа на определенное задание"""
    exercise: ExerciseSchema


class UpdateExerciseResponseSchema(BaseModel):
    """Описание структуры ответа по обновленным полям"""
    exercise: ExerciseSchema


class QueryExercisesSchema(BaseModel):
    """Словарь для айди курса"""
    courseId: str


class CreateExerciseRequestSchema(BaseModel):
    """Словарь для создания задания"""
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias='courseId', default_factory=fake.uuid4)
    max_score: int = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int = Field(alias='minScore', default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    order_index: int = Field(alias='orderIndex', default_factory=fake.integer)
    estimated_time: str = Field(alias='estimatedTime', default_factory=fake.estimated_time)


class UpdateExercisesRequestSchema(BaseModel):
    """Словарь для обновления задания"""
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int = Field(alias='orderIndex', default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)
