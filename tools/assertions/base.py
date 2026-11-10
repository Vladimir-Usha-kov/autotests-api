from typing import Any, Sized
import allure
from tools.loggers import get_logger

logger = get_logger('BASE_ASSERTIONS')

@allure.step('Check that response status code equals to {expected}')
def assert_status_code(actual: int, expected):
    """
    Проверят что факстический статус код соответствует ожидаемомму
    :param actual: Фактический статус код
    :param expected: Ожидаемый статус код
    :raises AssertionError: Если статус коды не совпадают
    """
    logger.info(f'Check that response status code equals to "{expected}"')
    assert actual == expected, (
        'Некорректный статус код, '
        f'Ожидаемый статус код: {expected} '
        f'Фактический статус код: {actual} '
    )
@allure.step('Check {name} equals to {expected}')
def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет что фактическое значение равно ожидаемому
    :param actual: Фактическое значение
    :param expected: Ожидаемое значение
    :param name: Название проверяемого значения
    :raises AssertionError: Если значение не совпадают
    """
    logger.info(f'Check "{name}" equals to {expected}')
    assert actual == expected, (
        f'Некорректное значение: {name}\n'
        f'Ожидаемое значение: {expected}\n'
        f'Фактическое значение: {actual}\n'
    )

@allure.step('Check {name} is true')
def assert_is_true(actual: Any, name: str):
    """
    Функция проверяет не пустое ли значение
    :param actual: Фактическое значение
    :param name: Название проверяемого значения
    :raises AsserrtionError: Если значение пустое
    """
    logger.info(f'Check "{name}" is true')
    assert actual, (
        f'Некорректное значение: {actual} '
        f'Корректное значение: {name}'

    )

def assert_length(actual: Sized, expected: Sized, name):
    """
    Проверяет, что длины двух объектов совпадают
    :param actual: Фактический объект
    :param expected: Ожидаемый объект
    :param name: Название проверяемого объекта
    :raises AssertionError: Если длины объектов не совпадают
    """
    with allure.step(f'Check that length to {name} equals to {len(expected)}'):
        logger.info(f'Check that length to "{name}" equals to {len(expected)}')
        assert len(actual) == len(expected), (
            f'Некорректная длина объекта: {name}'
            f'Ожидаемая длина объекта: {len(expected)}'
            f'Фактическая длина объекта: {len(actual)}'
        )