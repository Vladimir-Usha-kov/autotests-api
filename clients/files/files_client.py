import os.path

import allure
from httpx import Response
from clients.api_client import APIClient

from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from tools.routes import ApiRoutes


class FileClient(APIClient):
    """Клиент для работы с /api/v1/files"""

    @allure.step('GET file by id: {file_id}')
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод для получения данных о ранее загруженном файле по его идентификатору.

        :param file_id: Идентификатор файла
        :return: Возвращает ответ вида httpx.Response
        """
        return self.get(url=f'{ApiRoutes.FILES}/{file_id}')

    @allure.step('Create file')
    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Метод для загрузки файла на сервер.

        :param request: Словарь с ключами: filename, directory, upload_file
        :return: Возвращает ответ вида httpx.Response
        """
        if not os.path.exists(request.upload_file):
            raise FileNotFoundError(f'File not found: {request.upload_file}')

        return self.post(
            url=ApiRoutes.FILES,
            data=request.model_dump(by_alias=True, exclude={'upload_file'}),
            files={"upload_file": open(request.upload_file, 'rb')}
        )

    @allure.step('Delete file by id: {file_id}')
    def delete_file_api(self, file_id: str):
        """
        Метод для удаления файла по идентификатору.

        :param file_id: Идентификатор файла
        :return: Возвращает ответ вида httpx.Response
        """
        return self.delete(url=f'{ApiRoutes.FILES}/{file_id}')

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        response = self.create_file_api(request=request)
        return CreateFileResponseSchema.model_validate_json(response.text)

def get_files_client(user: AuthenticationUserSchema) -> FileClient:
    """
    Фунцкия создает эеземпляр FileClient с уже настроенным HTTP-клиентом
    :return: Готовый к использованию FileClient
    """
    return FileClient(client=get_private_http_client(user))

