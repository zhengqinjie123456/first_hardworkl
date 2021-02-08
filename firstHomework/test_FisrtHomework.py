import pytest
import yaml
from decimal import Decimal


def readYaml(path):
    # './YamlDir/YamlData.yaml'
    with open(path,encoding='utf-8') as f:
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
        print(firstNum,secNum,result)
        assert True

    @pytest.mark.parametrize("firstNum,secNum,result", datas["div"],ids=datas["ids"])
    def test_div(self, firstNum, secNum, result):

        with pytest.raises(ZeroDivisionError):
            # 当with下面程序执行后，捕获的异常跟上面一致时，则表示通过
            c   =firstNum/secNum

