from typing import List

import pytest
import yaml

@pytest.fixture(autouse=True)
def calcu():
    print("开始计算")
    yield
    print("计算结束")
#def pytest_collection_modifyitems(
#            session: "Session", config: "Config", items: List["Item"]
#    ) -> None:
#        print(items)
#        print(len(items))
#       print("teststseaerfesf")
#parser: 用户命令行参数与ini文件值的解析器
def pytest_addoption(parser):
    mygroup = parser.getgroup("ymtest")     #group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--envtest",    #注册一个命令行选项
                      default='test',
                      dest='envtest',
                      help='set your run env'
                      )
@pytest.fixture()
def cmdoption(request):
       myenv= request.config.getoption("--envtest", default='test')
       if myenv=='test':
           datapath='D:/untitled/datas/test/data.yml'
       if myenv=='dev':
           datapath='D:/untitled/datas/dev/data.yml'
       if myenv=='st':
           datapath='D:/untitled/datas/st/data.yaml'
       with open(datapath) as f:
           datas=yaml.safe_load(f)
           return myenv,datas

