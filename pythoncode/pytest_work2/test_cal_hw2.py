import pytest
import yaml

def getdata():
    with open ("./calc2.yml") as f:
        datas_yml = yaml.safe_load(f)
    return datas_yml

class TestCal:
    @pytest.mark.parametrize(("a","b"), getdata().get("add"), ids=[
        "整数", "浮点数", "负数","大数"
    ])
    @pytest.mark.dependency()
    @pytest.mark.run(order=1)
    def test_add(self, a, b,setup_cal):
        print("加法")
        print(f"{a} + {b} = {setup_cal.add(a,b)}")
        assert a + b == setup_cal.add(a,b)

    @pytest.mark.parametrize(("a", "b"), getdata().get("sub"), ids=[
        "整数", "浮点数", "负数","大数"
    ])
    @pytest.mark.dependency(depends=["test_add"])
    @pytest.mark.run(order=2)
    def test_sub(self, a, b,setup_cal):
        print("减法")
        print(f"{a} - {b} = {setup_cal.add(a, b)}")
        assert a - b == setup_cal.sub(a, b)

    @pytest.mark.parametrize(("a", "b"), getdata().get("mul"), ids=[
        "整数", "浮点数", "负数","大数"
    ])
    @pytest.mark.dependency()
    @pytest.mark.run(order=3)
    def test_mul(self, a, b,setup_cal):
        print("乘法")
        print(f"{a} * {b} = {setup_cal.add(a, b):.2f}")
        assert a * b == setup_cal.mul(a, b)

    @pytest.mark.parametrize(("a", "b"), getdata().get("div"), ids=[
        "整数", "浮点数", "取0","大数"
    ])
    @pytest.mark.dependency(depends=["test_mul"])
    @pytest.mark.run(order=4)
    def test_div(self, a, b,setup_cal):
        print("除法")
        print(f"{a} / {b} = {setup_cal.add(a, b):.2f}")
        assert a / b == setup_cal.div(a, b)
