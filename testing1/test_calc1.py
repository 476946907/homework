from typing import List

import pytest
import yaml
from decimal import *
import sys
sys.path.append("..")
from pythoncode1.calc1 import Calculator


with open('./data.yaml') as f:
     mydata=yaml.safe_load(f)
     myadd= mydata['add']
     mysub = mydata['sub']
     mymul = mydata['mul']
     mydiv = mydata['div']

def test_case(cmdoption):
    print("测试环境验证")
    env, datas = cmdoption
    print(f"环境：{env}，数据：{datas}")
    #    ip=str(datas['env']['ip'])
    # print(ip)




class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
#    @pytest.mark.parametrize(['a', 'b', 'result'], yaml.safe_load(open('./data.yaml'))['sub'],
#                            ids=['int', 'big num', 'xiaoshu', 'fushu'])
# 减法
    @pytest.mark.run(order=2)
   # @pytest.mark.dependency(depends=["check_add"])

    @pytest.mark.parametrize(['a', 'b', 'result'], mysub,
                                 ids=['int', 'big num', 'xiaoshu', 'fushu'])
    def check_sub(self, a, b, result):
            assert Decimal(result) == self.cal.sub(a, b)

    #加法
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(['a', 'b', 'result'], myadd,
                             ids=['int', 'big num', 'xiaoshu', 'fushu', 'xiaoshu1'])
    def check_add(self, a, b, result):
        assert Decimal(result) == self.cal.add(a, b)

#除法
    @pytest.mark.run(order=4)
    #@pytest.mark.dependency(depends=["check_mul"])

    @pytest.mark.parametrize(['a', 'b', 'result'], mydiv,ids=['int', 'big num', 'xiaoshu', 'fushu'])

    def check_div(self, a, b, result):
        assert Decimal(result) == self.cal.div(a, b)
#乘法
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize(['a', 'b', 'result'], mymul,
                                 ids=['int', 'big num', 'xiaoshu', 'fushu'])
    def check_mul(self, a, b, result):
         assert Decimal(result) == self.cal.mul(a, b)

    def test_f(self):
          print("test")




