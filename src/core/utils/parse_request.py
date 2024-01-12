from flask import Request
from werkzeug.exceptions import BadRequest

from core.logger import logger


def parse_request(request: Request) -> dict[str, str]:
    try:
        request_data = request.get_json(force=True)
    except BadRequest:
        request_data = request.form.to_dict()

    logger.info('Request URL %s', request.base_url)
    logger.info('Request_data: %s', request_data)

    return request_data
