import pytest
from calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(2, 3) == 5
    assert calc.subtract(2, 3) == -1
    assert calc.divide(10, 2) == 5
    assert calc.multiply(10, 2) == 20

def test_divide_by_zero():
   with pytest.raises(ZeroDivisionError):
       calc.divide(5, 1)
