import pytest


@pytest.fixture(scope='function')
def say_hello():
    print('hello')
    return 14
