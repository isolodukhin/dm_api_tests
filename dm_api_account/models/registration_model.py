from pydantic import BaseModel, StrictStr, Field


class RegistrationModel(BaseModel):
    login: StrictStr = Field(default='test')
    email: StrictStr = Field(alias='email')
    password: StrictStr = Field(alias='password')

