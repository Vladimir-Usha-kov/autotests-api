from clients.error_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
import allure
from tools.loggers import get_logger

logger = get_logger('ERRORS_ASSERTION')

@allure.step('Check validation error')
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Проверяет, что объект ошибки валидации соответствует ожидаемым значениям
    :param actual: Фактическая ошибка
    :param expected: Ожидаемая ошибка
    :return AssertionError: Если значение полей не совпадает
    """
    logger.info('Check validation error')

    assert_equal(actual.type, expected.type, 'type')
    assert_equal(actual.location, expected.location, 'location')
    assert_equal(actual.message, expected.message, 'message')
    assert_equal(actual.input, expected.input, 'input')
    assert_equal(actual.context, expected.context, 'context')

@allure.step('Check validation error response')
def assert_validation_error_response(
        actual: ValidationErrorResponseSchema,
        expected: ValidationErrorResponseSchema):
    """
    Проверяет, что объект ответа API с ошибками валидации "ValidationErrorResponseSchema"
    соответствует ожидаемому значению
    :param actual: Фактический ответ API
    :param expected: Ожидаемый ответ API
    :raises AssertionError: Если значения не совпадают
    """
    logger.info('Check validation error response')
    assert_length(actual.details, expected.details, 'details')

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)

@allure.step('Check internal error response')
def assert_internal_error_response(actual: InternalErrorResponseSchema, expected: InternalErrorResponseSchema):
    """
    Функция для проверки внутренней ошибки. Например, ошибки 404 (File not found)
    :param expected: Ожидаемый ответ от API
    :param actual: Фактический ответ от API
    :raises AssertionError: Если значений полей не совпадают
    """
    logger.info('Check internal error response')
    assert_equal(actual.details, expected.details, 'details')