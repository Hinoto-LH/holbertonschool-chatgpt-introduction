#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Vérification du nombre d'arguments
if len(sys.argv) != 2:
    print("Usage : python3 script.py <nombre>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    result = factorial(number)
    print(result)
except ValueError as e:
    print("Erreur :", e)