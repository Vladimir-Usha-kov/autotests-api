from clients.authentication.authentication_schema import LoginResponseSchema
import allure
from tools.assertions.base import assert_is_true, assert_equal
from tools.loggers import get_logger

logger = get_logger('AUTHENTICATION_ASSERTIONS')

@allure.step('Check login response')
def assert_login_response(response: LoginResponseSchema):
    """
    Функция проверяет корректность ответа после авторизации пользователя
    :param response: Объект ответа токена авторизации
    :raises AssertionError: Если какое либо условие не выполняется
    """
    logger.info('Check login response')
    assert_equal(response.token.token_type, 'bearer', 'tokenType')
    assert_is_true(response.token.access_token, 'accessToken')
    assert_is_true(response.token.refresh_token, 'refreshToken')
