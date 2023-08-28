from pydantic import BaseModel, StrictStr, Field


class ChangePasswordModel(BaseModel):
    login: StrictStr = Field(default='test')
    email: StrictStr = Field(alias='email')
    password: StrictStr = Field(alias='password')
    oldPassword: StrictStr = Field(alias='passwordd')