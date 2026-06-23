from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict

from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class File(TypedDict):
    """
    Описание стуктуры файла
    """
    id: str
    url: str
    filename: str
    directory: str


class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла
    """
    filename: str
    directory: str
    upload_file: str

class CreateFileResponse(TypedDict):
    """
    Описание структуры ответа создания файла
    """
    file: File

class FileClient(APIClient):
    """Клиент для работы с /api/v1/files"""

    def get_file_api(self, file_id: str) -> Response:
        """
        Метод для получения данных о ранее загруженном файле по его идентификатору.

        :param file_id: Идентификатор файла
        :return: Возвращает ответ вида httpx.Response
        """
        return self.get(url=f'/api/v1/files/{file_id}')

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод для загрузки файла на сервер.

        :param request: Словарь с ключами: filename, directory, upload_file
        :return: Возвращает ответ вида httpx.Response
        """
        return self.post(
            url='/api/v1/files',
            data=request,
            files={"upload_file": open(request["upload_file"], 'rb')}
        )

    def delete_file_api(self, file_id: str):
        """
        Метод для удаления файла по идентификатору.

        :param file_id: Идентификатор файла
        :return: Возвращает ответ вида httpx.Response
        """
        return self.delete(url=f'/api/v1/files/{file_id}')

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponse:
        response = self.create_file_api(request=request)
        return response.json()

def get_files_client(user: AuthenticationUserDict) -> FileClient:
    """
    Фунцкия создает эеземпляр FileClient с уже настроенным HTTP-клиентом
    :return: Готовый к использованию FileClient
    """
    return FileClient(client=get_private_http_client(user))

