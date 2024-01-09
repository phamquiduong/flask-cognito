from pydantic import BaseModel


class ErrorField(BaseModel):
    field: str
    message: str


class ErrorResponseSchema(BaseModel):
    status_code: int
    code: str
    message: str | None
    error_code: str | None
    error_fields: list[ErrorField] | None = None
