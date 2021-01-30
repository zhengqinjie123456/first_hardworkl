import pytest
import yaml
from decimal import Decimal


def readYaml(path):
    # './YamlDir/YamlData.yaml'
    with open(path) as f:
        result = yaml.safe_load(f)
    return result


datas: dict = readYaml('./YamlDir/YamlData.yaml')




class Test_calculate():
    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize("firstNum,secNum,result", datas["add"])
    def test_add(self, firstNum, secNum, result):
        Sum = firstNum + secNum
        NewSum = float(Decimal(Sum).quantize(Decimal("0.0001")))
        assert float(result) == NewSum

    @pytest.mark.parametrize("firstNum,secNum,result", datas["div"])
    def test_div(self, firstNum, secNum, result):
        try:
            Div = firstNum / secNum
        except Exception as e:
            print(f"数值类型或者值有误：{e}")
        NewDiv = float(Decimal(Div).quantize(Decimal("0.0001")))
        assert float(result) == NewDiv
