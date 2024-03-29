from werkzeug.exceptions import HTTPException

from core.errors.api_exception import APIException


def http_exception_handler(exc: HTTPException):
    return APIException(message=exc.description, status=exc.code).dump_response()


def exception_handler(exc: Exception):
    return APIException(message=str(exc)).dump_response()
