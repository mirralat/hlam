import requests
from config import url
from tpo.src.enums.global_enums import GlobalErrorMessages


def test_getting_data():
    response = requests.get(url=url)
    received_data = response.json()
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE
    assert len(received_data) == 3, GlobalErrorMessages.WRONG_JSON_COUNT
