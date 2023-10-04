from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Statuses, UserErrors
import re


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders     # делаем два доступных типа поля через enum
    status: Statuses

    @validator('email')
    def validate_email(cls, email):
        pattern = '^\w{0,}@{1}\w{0,}\.\w{0,}$'
        if re.match(pattern, email):
            return email
        raise ValueError(UserErrors.value)

