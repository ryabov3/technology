from calculator import Calculator

def test_calculator():
    calculator = Calculator()
    assert calculator.add(10, 2) == 10, "Ошибка в сложении чисел"
    assert calculator.subtract(10, 2) == 8, "Ошибка в вычитании чисел"
    assert calculator.divide(10, 2) == 5, "Ошибка в делении чисел"
    assert calculator.multiply(10, 2) == 20, "Ошибка в умножении чисел"

test_calculator()
