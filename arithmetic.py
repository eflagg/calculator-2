def add(num1, num2):
    """Add two numbers

    Add together num1 and num2, returning results
    """

    return num1 + num2


def subtract(num1, num2):
    """Subtract two numbers

    Subtract num2 from num1, returning results
    """

    return num1 - num2


def multiply(num1, num2):
    """Multiply two numbers

    Multiply together num1 and num2, returning results
    """

    return num1 * num2


def divide(num1, num2):
    """Divide two numbers

    Reassign num1 and num2 from integers to floats. Divide num1 by num2, returning floated results
    """

    num1 = float(num1)
    num2 = float(num2)

    return num1 / num2


def square(num1):
    """Square one number

    Raise num1 to the second power, returning results
    """

    return num1 ** 2


def cube(num1):
    """Cube one number

    Raise num1 to the power of 3, returning results
    """

    return num1 ** 3


def power(num1, num2):
    """Raise 1 number to the power of another number

    Raise num1 to the power of num2, returning results
    """

    return num1 ** num2


def mod(num1, num2):
    """Find remainder

    Divide integers, num1 from num2, returning remainder 
    """

    return num1 % num2
