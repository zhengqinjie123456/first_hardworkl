import pytest
import yaml


def readYaml(path):
    # './YamlDir/YamlData.yaml'
    with open(path) as f:
        result = yaml.safe_load(f)
    return result
datas=readYaml('./YamlDir/YamlData.yaml')

class Test_calculate():




    @pytest.mark.parametrize("firstNum,secNum,result",[datas])
    def test_add(self,firstNum,secNum,result):
        print(f'这是yaml读取的数据{datas}')
        assert result == firstNum + secNum

    # @pytest.mark.parametrize("firstNum,secNum,result", [datas])
    # def test_div(self,firstNum,secNum,result):
    #     assert result == firstNum / secNum
