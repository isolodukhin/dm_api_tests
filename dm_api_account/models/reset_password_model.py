from pydantic import BaseModel, StrictStr, Field


class ResetPasswordModel(BaseModel):
    login: StrictStr = Field(default='test')
    email: StrictStr = Field(alias='email')
