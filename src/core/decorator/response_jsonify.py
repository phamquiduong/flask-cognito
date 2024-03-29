from http import HTTPStatus
from typing import Any

from flask import Response, jsonify
from pydantic import BaseModel, ValidationError
from werkzeug.exceptions import HTTPException

from core.errors.api_exception import APIException, BadRequestException
from core.logger import logger


def response_jsonify(status_code: HTTPStatus | int = HTTPStatus.OK, api_code: int = 0):
    def inner(func):
        def wrapper(*args, **kwargs):
            try:
                response = func(*args, **kwargs)
            except ValidationError as valid_error:
                logger.error(valid_error)
                error_fields = {str(next(iter(error["loc"]), '__all__')): error["msg"]
                                for error in valid_error.errors()}
                return BadRequestException(api_code=api_code, error_fields=error_fields,
                                           message='Invalid request data').dump_response()
            except APIException as api_exc:
                logger.error(api_exc)
                api_exc.api_code = api_code
                return api_exc.dump_response()
            except HTTPException as http_exc:
                logger.error(http_exc)
                return APIException(api_code=api_code, status=http_exc.code,
                                    message=http_exc.description).dump_response()
            except Exception as exc:                                    # pylint: disable=broad-except
                logger.error(exc)
                return APIException(api_code=api_code, message=str(exc)).dump_response()

            return __get_response(response)

        def __get_response(response):
            if type(response) is Response | tuple[Response, Any]:       # pylint: disable=C0123
                return response
            if isinstance(response, BaseModel):
                return jsonify(response.model_dump()), status_code
            return jsonify(response), status_code

        wrapper.__name__ = func.__name__
        return wrapper
    return inner
