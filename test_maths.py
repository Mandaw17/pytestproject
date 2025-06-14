import pytest
from maths import Mathematics

class TestMathematics:

    def data_provider():
        return [
            (1, 2, 3),
            (0, 0, 0),
            (-1, 1, 0),
            (100, 200, 300),
            (-50, -50, -100)
        ]

    @pytest.mark.parametrize("a, b, expected", data_provider())
    def test_addition(self, a, b, expected):

        m = Mathematics()
        result = m.add(a, b)
        assert  result == expected