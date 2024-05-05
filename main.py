def add_numbers(numbers):
    """
    Adds all the numbers in the given list and returns the sum.
    """
    return sum(numbers)

def subtract_numbers(numbers):
    """
    Subtracts all the numbers in the given list from the first number and returns the result.
    """
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result