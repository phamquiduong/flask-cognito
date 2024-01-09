from http import HTTPStatus

from flask import jsonify
from werkzeug.exceptions import HTTPException

from core.schema.error_response import ErrorField, ErrorResponseSchema


class APIException(HTTPException):
    STATUS: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, message: str | None = None,
                 api_code: int = 0,
                 error_code: int = 0,
                 error_fields: dict[str, str] | None = None) -> None:
        super().__init__(description=message)
        self.api_code = api_code
        self.error_code = error_code
        self.error_fields = error_fields

    def dump(self, exclude_none: bool = True):
        error_fields = [ErrorField(field=field, message=msg) for field, msg in self.error_fields.items()] \
            if self.error_fields is not None else None

        return ErrorResponseSchema(
            status_code=self.STATUS,
            code=self.STATUS.phrase,

            error_code=f'ERR-{self.STATUS}-{self.api_code:03d}-{self.error_code:03d}',
            message=self.description or self.STATUS.description,

            error_fields=error_fields
        ).model_dump(exclude_none=exclude_none)

    def dump_json(self, exclude_none: bool = True):
        return jsonify(self.dump(exclude_none))

    def dump_response(self, exclude_none: bool = True):
        return self.dump_json(exclude_none), self.STATUS


class BadRequestException(APIException):
    STATUS = HTTPStatus.BAD_REQUEST


class UnauthorizedException(APIException):
    STATUS = HTTPStatus.UNAUTHORIZED


class ForbiddenException(APIException):
    STATUS = HTTPStatus.FORBIDDEN


class NotFoundException(APIException):
    STATUS = HTTPStatus.NOT_FOUND


class MethodNotAllowedException(APIException):
    STATUS = HTTPStatus.METHOD_NOT_ALLOWED


class ConflictException(APIException):
    STATUS = HTTPStatus.CONFLICT
