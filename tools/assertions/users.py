import allure

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema, \
    UserSchema
from tools.assertions.base import assert_equal
from tools.loggers import get_logger

logger = get_logger('USER_ASSERTION')

@allure.step('Check create user response')
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу
    :param request: Исходный запрос на создание пользователя
    :param response: Ответ API с данными пользователя
    :raises AssertionError: Если хотя бы одно поле не совпадает
    """
    logger.info('Check create user response')
    assert_equal(response.user.email, request.email, 'email')
    assert_equal(response.user.first_name, request.first_name, 'first_name')
    assert_equal(response.user.middle_name, request.middle_name, 'middle_name')
    assert_equal(response.user.last_name, request.last_name, 'last_name')

@allure.step('Check user')
def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет что данные запрашиваемого пользователя соответсвует созданному пользователю
    :param actual: Фактическое значение
    :param expected: Ожидаемое значение
    :raise AssertionError: Если значения не совпадают
    """
    logger.info('Check user')
    assert_equal(actual.id, expected.id, 'email')
    assert_equal(actual.email, expected.email, 'id')
    assert_equal(actual.first_name, expected.first_name, 'first_name')
    assert_equal(actual.middle_name, expected.middle_name, 'middle_name')
    assert_equal(actual.last_name, expected.last_name, 'last_name')

@allure.step('Check get user response')
def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """
    Проверяет что ответ на запрос пользователя соответсвует созданному пользователю
    :param get_user_response: Ответ API по запрашиваемому пользователю
    :param create_user_response: Ответ API по созданному пользователю
    :raises AssertionError: Если ответы не совпадают
    """
    logger.info('Check get user response')
    assert_user(get_user_response.user, create_user_response.user)
