
import pytest
from file import str_to_int_list


@pytest.mark.parametrize("str_lst", [
    # определяем значения, которые будет
    # принимать переменная `str_lst``
    ['8.3', '11', 'девять', '1', '5', '3'],
    ['пять', '-1', '-13', '7', '3.9', '4'],
    ['5ять', '1,5', '6.3', '2,0', 'два', '9']
])
class Test_str_to_int_list():

    def test_is_list(self, str_lst):
        result = str_to_int_list(str_lst)
        assert isinstance(result, list)

    def test_int_to_list(self, str_lst):
        result = str_to_int_list(str_lst)
        assert all([isinstance(n, int) for n in result])

    def test_0_10(self, str_lst):
        result = str_to_int_list(str_lst)
        assert all([0 <= n <= 10 for n in result])



@pytest.mark.parametrize("str_lst", [[], ['1.ин', 'два', 'три', 'четыре']])
def test_empty_list(str_lst):
    result = str_to_int_list(str_lst)
    assert result == []
