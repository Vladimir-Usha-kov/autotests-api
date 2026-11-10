from httpx import Request, Response
import allure
from tools.http.curl import make_curl_from_request
from tools.loggers import get_logger

logger = get_logger('HTTP_CLIENT')

def curl_event_hooks(request: Request):
    """
    Event hook для автоматического прикрепления cURL команды к Allure отчету
    :param request: HTTP-запрос, переданный в 'httpx' клиент
    """
    curl_command = make_curl_from_request(request)

    allure.attach(curl_command, 'cURL command', allure.attachment_type.TEXT)


def log_request_event_hook(request: Request):
    """
    Event hook логирует информацию об отправленном HTTP-запросе
    :param request: Объект запроса HTTPX
    """
    return logger.info(f'Make {request.method} to request {request.url}')


def log_response_event_hook(response: Response):
    """
    Event hook логирует информацию о полученном HTTP-ответе
    :param response: Объект ответа HTTPX
    """
    return logger.info(
        f'Got response {response.status_code} {response.reason_phrase} from {response.url}')