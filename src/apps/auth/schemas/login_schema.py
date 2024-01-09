from pydantic import BaseModel, EmailStr, model_validator


class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    new_password: str | None = None

    @model_validator(mode='after')
    def check_passwords_match(self) -> 'LoginRequest':
        if self.new_password is not None and self.password == self.new_password:
            raise ValueError('New password must not be them same as old password')
        return self


class LoginResponse(BaseModel):
    access_token: str
