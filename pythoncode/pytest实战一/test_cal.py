import pytest

from pythoncode.pytest实战一.cal import Calculator

#类外面的def定义叫函数，类里面的叫方法
def test_a():
    print("testa")

def setup_module():
    print("steup module")

def teardown_module():
    print("teardown module")

# def setup_function():
#     print("steup function")
#
# def teardown_function():
#     print("teardown function")

class TestCal:

    # def setup_class(self):
    #     self.cal = Calculator()     #setup类里初始化
    #     print("setup class")
    #
    # def teardown_class(self):
    #     print("teardown class")


    # def setup(self):
    #     self.cal = Calculator()     #setup类里初始化
    #     print("setup")
    #
    # def teardown(self):
    #     print("teardown")

    @pytest.mark.add  #测试用例标记，用于“-m”测试用例标记，类似“-k”
    def test_add(self):
        print("测试 相加")
        assert 3 == self.cal.add(1,2)

    @pytest.mark.skip #skip执行会跳过
    def test_add1(self):
        print("测试 相加1")
        assert 3 == self.cal.add(1, 2)

    @pytest.mark.sub
    def test_sub(self):
        print("测试 相减")
        assert 50 == self.cal.sub(80,30)

    @pytest.mark.mul
    def test_mul(self):
        print("测试 相乘")
        assert 63 == self.cal.mul(7,9)

    @pytest.mark.mul
    def test_mul1(self):
        print("测试 相乘1")
        assert 60 == self.cal.mul(7,9)

    def test_div(self):
        print("测试 相除")
        assert 2 == self.cal.div(2,1)

    @pytest.mark.xfail #xfail会执行，错误不会报错
    def test_div1(self):
        print("测试 相除1")
        assert 2 == self.cal.div(1,1)


