import pytest
from main import Calculator

def test_pytest_connection():
    assert True

def test_calculator_add():
    try:
        calculator = Calculator()
        assert calculator.add(1,3) == 4
        assert calculator.add(5,3) == 8
        assert calculator.add(11,14) == 25
        calculator.add('11', '12')
    except Exception as e:
        assert e.args[0] == "Both arguments must be an integer"

def test_calculator_multiply():
    try:
        cal = Calculator()
        assert cal.multiply(3, 3) == 9
        assert cal.multiply(4,3) == 12
        assert cal.multiply(10,10) == 100
    except Exception as e:
        assert e.args[0] == "Both arguments must be an integer"
    


