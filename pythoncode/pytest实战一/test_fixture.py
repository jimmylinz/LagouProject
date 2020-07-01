import pytest
# @pytest.fixture(autouse=True) #fixture用于前置工作的准备
# @pytest.fixture(scope='module')
# @pytest.fixture()
# @pytest.fixture(scope='class',params=[1,2,3,'lilili'])
# def login(request):
#     print("登录")
#     yield request.param
#     print("登出")
@pytest.fixture()
def login(request):
    print("开始计算")
    yield ['name','123']
    print("计算结束")

def test_case0(login):
    print("testcase 0")

class TestLogin:

    def test_case1(self, login):
        print("testcase 1")

    def test_case2(self,login):
        print("testcase 2")

    def test_case3(self,login):
        print("testcase 3")

#    @pytest.mark.usefixtures('login') #另一种调用方法
#     def test_case1(self,login1):
#         print(login1)
#         print("testcase 1")