#被测试模块
#实现计算
from decimal import Decimal
class  Calculator:
    def add(self,a,b):
        return Decimal(a)+Decimal(b)
    def div(self,a,b):
        return Decimal(a) / Decimal(b)
    def sub(self,a,b):
        return Decimal(a)-Decimal(b)
    def mul(self,a,b):
        return Decimal(a)*Decimal(b)

