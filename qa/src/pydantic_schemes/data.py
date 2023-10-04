from pydantic import BaseModel, validator, ValidationError


class Data(BaseModel):
    id: int
    title: str

    @validator("id")
    def check_that_id_less_than_two(cls, v):
        if v > 2:
            raise ValidationError('id is not less than two')
        else:
            return v
