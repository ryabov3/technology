import pytest
from calculator import Calculator
from hypothesis import given
from hypothesis.strategies import integers

calculator = Calculator()

class TestCalculator:

    @given(integers(), integers())
    def test_add(self, a, b):
        assert calculator.add(a, b) == a + b

    @given(integers(), integers())
    def test_subtract(self, a, b):
        assert calculator.subtract(a, b) == a - b

    @given(integers(), integers())
    def test_divide(self, a, b):
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                calculator.divide(a, b)
        else:
            assert calculator.divide(a, b) == a / b

    @given(integers(), integers())
    def test_multiply(self, a, b):
        assert calculator.multiply(a, b) == a * b




