from pydantic import BaseModel, EmailStr


class GetUserRequest(BaseModel):
    access_token: str


class GetUserResponse(BaseModel):
    email: EmailStr
    email_verified: bool = False
    sub: str
