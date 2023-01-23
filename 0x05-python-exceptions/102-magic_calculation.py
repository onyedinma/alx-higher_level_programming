#!/usr/bin/python3
# 102-magic_calculation.py
# Onyedinma Onyekachi <onyedinmaonyekachi@gmail.com>


def magic_calculation(a, b):
    """
    This function performs a calculation using the values of a and b.
    """
    # Initialize result to 0
    result = 0
    # Loop through the range of 1 and 3 (not including 3)
    for i in range(1, 3):
        try:
            # If i is greater than a, raise an exception
            if i > a:
                raise Exception("Too far")
            else:
                # Add the result of (a ** b) / i to the result variable
                result += (a ** b) / i
        except:
            # If an exception is raised, add a + b to the result variable
            result += a + b
    # Return the final result
    return result

