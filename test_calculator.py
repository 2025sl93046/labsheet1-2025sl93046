import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_sub():
    assert calculator.subtract(5, 3) == 2

def test_mul():
    assert calculator.multiply(2, 3) == 6

def test_div():
    assert calculator.divide(6, 3) == 2

test_add()
test_sub()
test_mul()
test_div()

print("All tests passed!")
