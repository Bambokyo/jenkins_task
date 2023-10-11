from trying import *
import pytest

calculator = Calculator()

# Test cases for the Calculator class
def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(1, 1) == 0
    assert calculator.subtract(0, 0) == 0


# Run the tests with PyTest
if __name__ == "__main__":
    pytest.main()
