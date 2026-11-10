import httpx
import allure
from config import settings
from clients.error_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetResponseFileSchema, \
    FileSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response
from tools.loggers import get_logger

logger = get_logger('FILE_ASSERTION')

@allure.step('Check file response')
def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на создание файла соответствует запросу

    :param request: Исходный запрос на создание файла
    :param response: Ответ API с данными файла
    :return AssertionError: Если хотя бы одно поле не совпадает
    """

    expected_url = f'{settings.http_client.client_url}static/{request.directory}/{request.filename}'
    logger.info('Check file response')
    assert_equal(str(response.file.url), expected_url, 'url')
    assert_equal(response.file.filename, request.filename, 'filename')
    assert_equal(response.file.directory, request.directory, 'directory')

@allure.step('Check file accessible to {url}')
def assert_file_is_accessible(url: str):
    """
    Проверяет, что файл достпуен по указанному URL

    :param url: Ссылка на файл
    :return AssertionError: Если файл не доступен
    """
    response = httpx.get(url=url)
    logger.info(f'Check file accessible to {url}')
    assert response.status_code == 200, f'Файл не доступен по URL: {url}'

@allure.step('Check file')
def assert_file(request: FileSchema, response: FileSchema):
    """
    Проверяем что фактические данные файла соответствуют ожидаемым

    :param request: Фактические данные файла
    :param response: Ожидаемые данные файла
    :return AssertionError: Если данные не совпадают
    """
    logger.info('Check file')
    assert_equal(request.id, response.id, 'id')
    assert_equal(request.url, response.url, 'url')
    assert_equal(request.filename, response.filename, 'filename')
    assert_equal(request.directory, response.directory, 'directory')

@allure.step('Check get file response')
def assert_get_file_response(*,
                             get_file_response: GetResponseFileSchema,
                             create_file_response: CreateFileResponseSchema
                             ):
    """
    Проверяет, что ответ на получение файла соответствует ответу на его создание

    :param get_file_response: Ответ API при запросе данный файла
    :param create_file_response: Ответ API при создание файла
    :return AssertionError: Если данные файла не совпадают
    """
    logger.info('Check get file response')
    assert_file(request=get_file_response.file, response=create_file_response.file)

@allure.step('Check create file with empty filename response')
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить
    :raises AssertionErrors: Если фактический ответ не соответсвтует ожидаемому
    """
    logger.info('Check create file with empty filename response')
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                location=["body", "filename"],
                message="String should have at least 1 character",
                input="",
                context={"min_length": 1}
            )
        ]
    )

    assert_validation_error_response(actual, expected)

@allure.step('Check create file with empty directory response')
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что создание файла с пустым значением дериктории соответствует ожидаемой валидационной ошибке

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить
    :raises AssertionErrors: Если фактический ответ не соответсвтует ожидаемому
    """
    logger.info('Check create file with empty directory response')
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                location=["body", "directory"],
                message="String should have at least 1 character",
                input="",
                context={"min_length": 1}
            )
        ]
    )

    assert_validation_error_response(actual, expected)

@allure.step('Check file not found response')
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция, для проверки ошибки, если файл не найден

    :param actual: Фактический ответ
    :return AssertionErrors: Если фактический ответ не соответсвует ошибке "File not found"
    """
    logger.info('Check file not found response')
    expected = InternalErrorResponseSchema(details='File not found')
    assert_internal_error_response(actual, expected)

@allure.step('Check get file with incorrect file id response')
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что созданный файл с некорректный file_id соответствует ожидаемому ответу
    :param actual: Фактический ответ от API
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому
    """
    logger.info('Check get file with incorrect file id response')
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type='uuid_parsing',
                location=['path', 'file_id'],
                message='Input should be a valid UUID, invalid character: '
                        'expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1',
                input='incorrect-file-id',
                context={"error": "invalid character: expected an optional"
                                  " prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"}
            )
        ]
    )

    assert_validation_error_response(actual, expected)
