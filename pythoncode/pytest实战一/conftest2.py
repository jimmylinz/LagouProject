import pytest


@pytest.fixture(scope='session')
def login():
    print("登录")
    return ['name','123']