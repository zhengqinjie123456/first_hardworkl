import pytest
import yaml
from decimal import Decimal


def readYaml(path):
    # './YamlDir/YamlData.yaml'
    with open(path) as f:
        result = yaml.safe_load(f)
    return result


datas: dict = readYaml('./YamlDir/YamlData.yaml')
print(datas)




class Test_calculate():
    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize("firstNum,secNum,result", datas["add"],ids=datas["ids"])
    def test_add(self, firstNum, secNum, result):

        assert c

    @pytest.mark.parametrize("firstNum,secNum,result", datas["div"],ids=datas["ids"])
    def test_div(self, firstNum, secNum, result):
        if secNum!=0:
            assert Decimal(str(result)) == Decimal(str(firstNum)) / Decimal(str(secNum))
        else:
            try:
                Div = firstNum / secNum
            except Exception as e:
                print(f"数值类型或者值有误：{e}")
            finally:
                assert True

