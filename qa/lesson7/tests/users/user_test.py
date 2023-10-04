import requests
from lesson5.tests.config import url
from src.baseclasses.response import Status
from src.schemas.user import User


def test_getting_user_list():
    response = requests.get(url)
    test_object = Status(response)
    test_object.assert_status_code(200).validate(User)
