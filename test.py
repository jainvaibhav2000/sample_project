from main import add_numbers, subtract_numbers

# Test cases for add_numbers function
def test_add_numbers():
    assert add_numbers([1, 2, 3]) == 6
    assert add_numbers([10, 20, 30, 40]) == 100
    assert add_numbers([-1, 0, 1]) == 0

# Test cases for subtract_numbers function
def test_subtract_numbers():
    assert subtract_numbers([10, 2, 3]) == 6
    assert subtract_numbers([100, 20, 30, 40]) == 10
    assert subtract_numbers([5, 2, 1]) == 2
