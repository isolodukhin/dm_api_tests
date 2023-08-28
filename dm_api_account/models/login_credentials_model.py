from pydantic import BaseModel, StrictStr, Field


class LoginCredentialsModel(BaseModel):
    login: StrictStr = Field(default='test')
    password: StrictStr = Field(alias='password')
    rememberMe: bool

