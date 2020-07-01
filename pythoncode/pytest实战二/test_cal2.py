import pytest
import yaml



# @pytest.mark.parametrize(("a", "b", "result"), yaml.safe_load(open("./calc.yml")))
from pythoncode.pytest实战二.cal2 import Calculator

def getdata():
    with open ("./calc.yml") as f:
        datas = yaml.safe_load(f)
    return datas

@pytest.mark.parametrize('a,b,result', getdata(),ids=[
    "整数","浮点数","bignum","miuns","float+int"
])
class TestCal:
    # def setup(self):
    #     self.cal = Calculator()
    #     print("setup")
    #
    # def teardown(self):
    #     print("teardown")

    # @pytest.mark.parametrize('a', [1, 2, 3])
    # @pytest.mark.parametrize('a', ["a","b","c"])
    # def test_add0(self, a, b):
    #     print(f"a = {a} b = {b}")

    # @pytest.mark.parametrize('a,b,result', [
    #     (1, 1, 2)
    #         (0.1, 0.1, 0.2)
    #         (1000, 1000, 2000)
    #         (-1, -1, -2)
    # ])
    # @pytest.mark.parametrize('a', pytest.param([1, 2, 3],id="int"))
    # @pytest.mark.parametrize('a', pytest.param(["a","b","c"],id="str"))
    # def test_add0(self, a, b):
    #     print(f"a = {a} b = {b}")
    @pytest.mark.dependency(name='first')
    @pytest.mark.run(order=1)
    def test_add(self, a, b, result,setup_cal):
        print("加法")
        assert result == setup_cal.add(a, b)


    def test_add1(self, a, b, result,setup_cal):
        print("加法")
        assert result == setup_cal.add(a, b)

    # @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("calc.yml")),ids=[
    #     "int","float","bignum","miuns","float+int"
    # ])
    # def test_add2(self, a, b, result):
    #     print("测试 相加")
    #     assert result == self.cal.add(a, b)
    # @pytest.mark.flaky(retuns=5,retuns_delay=1)
    # def test_add(self, a, b, result):
    #     print("测试 相加")
    #     assert result == self.cal.add(a, b)
    @pytest.mark.dependency(depends=["first"])
    @pytest.mark.run(order=2)
    def test_sub(self, a, b, result,setup_cal):
        print("减法")
        assert result == setup_cal.sub(a, b)

    @pytest.mark.dependency(name='second')
    @pytest.mark.run(order=3)
    def test_mul(self, a, b, result,setup_cal):
        print("乘法")
        assert result == setup_cal.mul(a, b)

    @pytest.mark.dependency(depends=["second"])
    @pytest.mark.run(order=4)
    def test_div(self, a, b, result,setup_cal):
        print("除法")
        assert result == setup_cal.div(a, b)
