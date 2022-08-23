def add(first_number: int, second_number: int) -> int:
    """
    Adds two numbers
    :param first_number: int
    :param second_number: int
    :return: int
    """

    return first_number + second_number

print(add(2,3))
print(add.__doc__)
print(add.__name__)
print(add.__annotations__)


def get_digit(number:int, position:int)-> int:
    """

    :param number:
    :param position:
    :return:
    """

    return number // (10**position) % 10

print(get_digit(1234,3))


def get_length(number: int)-> int:
    import math
    return math.ceil(math.log10(number))
   # return len(str(number))

print(get_length(12345))

