import allure
from clients.error_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExercisesResponseSchema, \
    GetExerciseResponseSchema, ExerciseSchema, UpdateExercisesRequestSchema, UpdateExerciseResponseSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response
from tools.loggers import get_logger

logger = get_logger('EXERCISES_ASSERTION')

@allure.step('Check create exercise response')
def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response: CreateExercisesResponseSchema
):
    """
    Проверяет, что ответ на создание задания соответсвует запросу

    :param request: Исходный запрос на создание задания
    :param response: Ответ от API
    :raises AssertionError: Если хотя бы одно поле не совпадает
    """
    logger.info('Check create exercise response')
    assert_equal(response.exercise.title, request.title, 'title')
    assert_equal(response.exercise.course_id, request.course_id, 'course_id')
    assert_equal(response.exercise.max_score, request.max_score, 'max_score')
    assert_equal(response.exercise.min_score, request.min_score, 'min_score')
    assert_equal(response.exercise.order_index, request.order_index, 'order_index')
    assert_equal(response.exercise.description, request.description, 'description')
    assert_equal(response.exercise.estimated_time, request.estimated_time, 'estimated_time')

@allure.step('Check exercise')
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные задания соответсвуют ожидаемым

    :param actual: Фактические данные
    :param expected: Ожидаемые данные
    :raises AssertionError: Если данные не совпадают
    """
    logger.info('Check exercise')
    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.title, expected.title, 'title')
    assert_equal(actual.course_id, expected.course_id, 'course_id')
    assert_equal(actual.max_score, expected.max_score, 'max_score')
    assert_equal(actual.min_score, expected.min_score, 'min_score')
    assert_equal(actual.order_index, expected.order_index, 'order_index')
    assert_equal(actual.description, expected.description, 'description')
    assert_equal(actual.estimated_time, expected.estimated_time, 'estimated_time')

@allure.step('Check get exercise response')
def assert_get_exercise_response(request: CreateExercisesResponseSchema, response: GetExerciseResponseSchema):
    """
    Проверяет, что ответ на получение задания соответсвует ответу на его создание

    :param request: Ответ API на создание задания
    :param response: Ответ API на получения задания
    :raises AssertionError: Если объекты не совпадают
    """
    logger.info('Check get exercise response')
    assert_exercise(request.exercise, response.exercise)

@allure.step('Check exercise not found response')
def assert_exercise_not_found(actual: InternalErrorResponseSchema):
    """
    Функция я проверки ошибки если задание не найдено

    :param actual: Фактический результат
    :raises AssertionError: Если ошибка не соответсвует "file not found"
    """
    logger.info('Check exercise not found response')
    expected = InternalErrorResponseSchema(detail='Exercise not found')
    assert_internal_error_response(actual, expected)

@allure.step('Check update exercise response')
def assert_update_exercise_response(request: UpdateExercisesRequestSchema, response: UpdateExerciseResponseSchema):
    """
    Проверяет, что запрос на обновление задания соответсвует данным из запроса
    :param request: Исходный запрос на обноление задания
    :param response: Ответ от API с обновленными данными задания
    :raises AssertionError: Если хотя бы одно поле не соответсвует
    """
    logger.info('Check update exercise response')
    assert_equal(response.exercise.title, request.title, 'title')
    assert_equal(response.exercise.max_score, request.max_score, 'max_score')
    assert_equal(response.exercise.min_score, request.min_score, 'min_score')
    assert_equal(response.exercise.order_index, request.order_index, 'order_index')
    assert_equal(response.exercise.description, request.description, 'description')
    assert_equal(response.exercise.estimated_time, request.estimated_time, 'estimated_time')

@allure.step('Check get exercise response')
def assert_exercises_get_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_response: list[CreateExercisesResponseSchema]
    ):
    """
    Проверяет, что ответ на получение списка заданий, соответствует ответам на их создания
    :param create_exercise_response: Ответ от API на создание задания
    :param get_exercises_response: Ответ от API на получение списка курсов
    :raises AssertionError: Если обекты не совпадают
    """
    logger.info('Check get exercise response')
    assert_length(get_exercises_response.exercises, create_exercise_response, 'exercises')

    for index, exercise in enumerate(create_exercise_response):
        assert_exercise(get_exercises_response.exercises[index], exercise.exercise)
