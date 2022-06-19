from Calculator import add
from Calculator import multiply
from Calculator import subtract
from Calculator import divide
import pytest


@pytest.fixture()
def create_list():
    return [10, 5]


@pytest.fixture()
def mul_text():
    print("fixture before multiply")


class TestCalc:

    def test_add(self, create_list):
        print(f'Input list {create_list}')
        assert add(create_list) == sum(create_list)

    def test_mul(self, mul_text):
        assert multiply(10, 5) == 10 * 5

    def test_sub(self):
        assert subtract(10, 5) == 10 - 5

    @pytest.mark.parametrize("a, b", [(10, 5), (20, 10)])
    def test_div(self, a, b):
        assert divide(a, b) == 10 / 5

    ########################################################

    @pytest.mark.xfail
    def test_add_neg(self, create_list):
        print(f'Input list {create_list}')
        assert add(create_list) == sum(create_list + 1)

    @pytest.mark.xfail
    def test_mul_neg(self, mul_text):
        assert multiply(10, 5) == 10 * 10

    @pytest.mark.xfail
    def test_sub_neg(self):
        assert subtract(10, 5) == 10 - 10

    @pytest.mark.skip
    @pytest.mark.parametrize("a, b", [(10, 5), (20, 10)])
    def test_div_neg(self, a, b):
        assert divide(a, b) == 10 / 5
