#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    ---------------------
    Calculates the factorial of a non-negative integer using recursion.

    Parameters:
    ----------
    n : int
        A non-negative integer whose factorial will be calculated.

    Returns:
    -------
    int
        The factorial of the given number n.

    Raises:
    ------
    ValueError
        If n is a negative integer.
    """
    # Check if the number is negative
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs")

    # Base case: factorial of 0 is 1
    if n == 0:
        return 1

    # Recursive case
    return n * factorial(n - 1)

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage : python3 script.py <nombre>")
    sys.exit(1)

try:
    # Convert the command-line argument to an integer
    number = int(sys.argv[1])

    # Calculate the factorial
    result = factorial(number)

    # Display the result
    print(result)
except ValueError as e:
    # Handle invalid input or negative numbers
    print("Erreur :", e)
