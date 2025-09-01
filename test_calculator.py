from calculator import Calculator

def test_add_two_positive():
    expected = 10
    result = Calculator.add(6, 4)
    assert result == expected

def test_add_two_negative():
    expected = -10
    result = Calculator.add(-6, -4)
    assert result == expected

def test_substract_two_positive():
    expected = 12
    result = Calculator.substract(30, 18)
    assert expected == result

def test_substract_two_negative():
    expected = -12 # -30 -(-18) => 12
    result = Calculator.substract (-30, -18)
    assert expected == result

def test_multiply_two_positive():
    expected = 24
    result = Calculator.multiply(6, 4)
    assert expected == result

def test_multiply_two_negative():
    expected = 24 # -30 -(-18) => 12
    result = Calculator.multiply (-6, -4)
    assert expected == result

def test_divide_two_positive():
    expected = 1.5
    result = Calculator.divide (6, 4)
    assert expected == result

def test_divide_two_negative():
    expected = 1.5 # -30 -(-18) => 12
    result = Calculator.divide (-6, -4)
    assert expected == result

def test_divide_zero():
    excepted = 