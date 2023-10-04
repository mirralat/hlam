import requests
from .conftest import say_hello


def test_getting_data(say_hello):
    print(say_hello)
