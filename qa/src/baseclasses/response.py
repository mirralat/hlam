from src.schemas.data import DATA_SCHEMA
from jsonschema import validate
from tpo.src.enums.global_enums import GlobalErrorMessages


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data')    # получаем данные запроса

    def validate(self, schema):
        if isinstance(self.response_json, list):  # для проверки вдруг там 1 объект
            for item in self.response_json:  # валидируем каждый объект по очереди
                validate(item, DATA_SCHEMA)
        else:
            validate(self.response_json, schema)
        return self


class Status:
    def __init__(self, response):
        self.response = response
        self.response_status = response.status_code

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WORNG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WORNG_STATUS_CODE.value
        return self
