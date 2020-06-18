import pytest
import yaml

from pythoncode.pytest_work1.cal_hw import Calculator

#@pytest.mark.parametrize(("a","b"), yaml.safe_load(open("data1.yml")))

class TestCal:
    @pytest.mark.parametrize(("a","b"), yaml.safe_load(open("data.yml")).get("add"))
    def test_add(self,setup_cal,a,b):
        print("加法")
        print(f"{a} + {b} = {setup_cal.add(a,b)}")
        assert a + b == setup_cal.add(a,b)

    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("data.yml")).get("sub"))
    def test_sub(self,setup_cal,a,b):
        print("减法")
        print(f"{a} - {b} = {setup_cal.sub(a, b)}")
        assert a - b == setup_cal.sub(a,b)

    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("data.yml")).get("mul"))
    def test_mul(self,setup_cal,a,b):
        print("乘法")
        print(f"{a} * {b} = {setup_cal.mul(a, b):.2f}")
        assert a * b == setup_cal.mul(a,b)

    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("data.yml")).get("div"))
    def test_div(self,setup_cal,a,b):
        print("除法")
        print(f"{a} / {b} = {setup_cal.div(a, b):.2f}")
        assert a / b == setup_cal.div(a,b)


