from http import HTTPStatus

from flask import jsonify
from werkzeug.exceptions import HTTPException

from core.schema.error_response import ErrorResponseSchema


class APIException(HTTPException):
    status: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, message: str | None = None,
                 status: int | None = None, api_code: int = 0, api_error_code: int = 0,
                 error_fields: dict[str, str] | None = None) -> None:
        super().__init__(description=message)

        if status is not None:
            self.status = HTTPStatus(status)
        self.api_code = api_code
        self.api_error_code = api_error_code
        self.error_fields = error_fields or {}

    def dump(self, exclude_none: bool = True):
        return ErrorResponseSchema(
            status_code=self.status,
            code=self.status.name,
            error_code=f'ERR-{self.status}-{self.api_code:03d}-{self.api_error_code:03d}',
            message=self.description or self.status.description,
            error_fields=[{'field': field, 'message': msg} for field, msg in self.error_fields.items()] or None
        ).model_dump(exclude_none=exclude_none)

    def dump_json(self, exclude_none: bool = True):
        return jsonify(self.dump(exclude_none))

    def dump_response(self, exclude_none: bool = True):
        return self.dump_json(exclude_none), self.status


class BadRequestException(APIException):
    status = HTTPStatus.BAD_REQUEST


class UnauthorizedException(APIException):
    status = HTTPStatus.UNAUTHORIZED


class ForbiddenException(APIException):
    status = HTTPStatus.FORBIDDEN


class NotFoundException(APIException):
    status = HTTPStatus.NOT_FOUND


class MethodNotAllowedException(APIException):
    status = HTTPStatus.METHOD_NOT_ALLOWED


class ConflictException(APIException):
    status = HTTPStatus.CONFLICT
