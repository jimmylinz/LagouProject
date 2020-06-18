from typing import List

import pytest
import yaml
from pythoncode.pytest_work2.cal2_hw import Calculator

""""""
@pytest.fixture(scope="session")
def setup_cal():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("计算结束")

#自定义的hook函数，pytest_collection_modifyitems可以将收集上来的测试用例进行改写
#控制用例的执行顺序，自动添加标签，解决测试用例的编码问题
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    #items 就是所有的测试用例列表，item代表每个测试用例对象
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
        elif 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)

def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption("--env",#注册一个命令行属性
                      default='test',
                      dest='env',
                      help='set your run env'
                         )
    mygroup.addoption("--env0",  # 注册一个命令行属性
                      default='dev',
                      dest='env0',
                      help='set your run env'
                      )
    mygroup.addoption("--env1",  # 注册一个命令行属性
                      default='st',
                      dest='env1',
                      help='set your run env'
                      )

@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env",default='test')
    if myenv == 'test':
        print("获取测试数据")
        with open("data/test/test.yml") as f:
            datas = yaml.safe_load(f)
    elif myenv == 'dev':
        print("获取dev数据")
        with open("data/dev/dev.yml") as f:
            datas = yaml.safe_load(f)
    elif myenv == 'st':
        print("获取st数据")
        with open("data/st/st.yml") as f:
            datas = yaml.safe_load(f)

    return datas