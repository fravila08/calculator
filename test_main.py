import pytest
from main import Calculator

def test_pytest_connection():
    assert True

def test_calculator_add():
    calculator = Calculator()
    assert calculator.add(1,3) == 4
    assert calculator.add(5,3) == 8
    assert calculator.add(11,14) == 25
