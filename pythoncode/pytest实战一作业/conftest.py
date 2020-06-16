import pytest

from pythoncode.pytest实战一作业.cal_hw import Calculator


@pytest.fixture(scope='session')
def setup_cal():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("计算结束")
