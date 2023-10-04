import requests
from config import url

from src.schemas.data import DATA_SCHEMA
from src.baseclasses.response import Response, Status


def test_getting_data():
    r = requests.get(url=url)
    response = Response(r)
    status = Status(r)
    status.assert_status_code(200)
    response.validate(DATA_SCHEMA)

