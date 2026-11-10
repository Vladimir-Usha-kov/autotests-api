from clients.courses.course_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, \
    GetCoursesResponseSchema, CourseSchema, CreateCourseResponseSchema, GetCourseIdResponseSchema, \
    CreateCourseRequestSchema
import allure
from tools.assertions.base import assert_equal
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user
from tools.loggers import get_logger

logger = get_logger('COURSE_ASSERTIONS')

@allure.step('Check update course response')
def assert_update_course_response(request: UpdateCourseRequestSchema, response: UpdateCourseResponseSchema):
    """
    Проверяет, что ответ на обновление курса соответствует данным из запроса
    :param request: Исходный запрос на обновление курса
    :param response: Ответ от API с обнавленными данными курса
    :raises AssertionError: Если данные не совпадают
    """
    logger.info('Check update course response')

    assert_equal(response.course.title, request.title, 'title')
    assert_equal(response.course.max_score, request.max_score, 'max_score')
    assert_equal(response.course.min_score, request.min_score, 'min_score')
    assert_equal(response.course.description, request.description, 'description')
    assert_equal(response.course.estimated_time, request.estimated_time, 'estimated_time')

@allure.step('Check course')
def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Проверяет, что фактические данные курса соответствуют ожидаемым

    :param actual: Фактические данные курса
    :param expected: Ожидаемые данные курса
    :raises AssertionError: Если хотя бы одно поле не совпадает
    """
    logger.info('Check course')
    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.title, expected.title, 'title')
    assert_equal(actual.max_score, expected.max_score, 'max_score')
    assert_equal(actual.min_score, expected.min_score, 'min_score')
    assert_equal(actual.description, expected.description, 'description')
    assert_equal(actual.estimated_time, expected.estimated_time, 'estimated_time')


    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)

@allure.step('Check get courses response')
def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_response: list[CreateCourseResponseSchema]
):
    """
    Проверяет, что ответ на получаение списка курсов соответсвует ответам на их создание
    :param get_courses_response: Ответ API при запросе списка курсов
    :param create_course_response: Ответ API при создании курсов
    :raises AssertionError: Если данные курсов не совпадают
    """
    logger.info('Check get courses response')
    for index, create_course_response in enumerate(create_course_response):
        assert_course(get_courses_response.courses[index], create_course_response.course)

@allure.step('Check get course id response')
def assert_get_course_id_response(
        update_course_response: UpdateCourseResponseSchema,
        get_id_course_response: GetCourseIdResponseSchema):
    """
    Пороверяем, что ответ на получение курса по id соответсвует отвут на его обновление
    :param update_course_response: Ответ API после обновления курса
    :param get_id_course_response: Ответ API запрашивамого курса
    :raises AsertionErrors: Если данные не совпадают
    """
    logger.info('Check get course id response')
    assert_course(update_course_response.course, get_id_course_response.course)

@allure.step('Check create course response')
def assert_create_course_response(request: CreateCourseRequestSchema, response: CreateCourseResponseSchema):
    """
    Проверяет, что ответ на создание курса соответсвует запросу
    :param request: Исходный запрос на создание курса
    :param response: Ответ от API с данными курса
    :raises AssertionError: Если хотя бы одно поле не совпадает
    """
    logger.info('Check create course response')
    assert_equal(response.course.title, request.title, 'title')
    assert_equal(response.course.max_score, request.max_score, 'max_score')
    assert_equal(response.course.min_score, request.min_score, 'min_score')
    assert_equal(response.course.description, request.description, 'description')
    assert_equal(response.course.estimated_time, request.estimated_time, 'estimated_time')

    assert_equal(response.course.preview_file.id, request.preview_file_id, 'preview_file_id')
    assert_equal(response.course.created_by_user.id, request.created_by_user_id, 'created_by_user_id')