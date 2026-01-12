#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # <--- On diminue n pour finir par sortir de la boucle
    return result

# Vérification qu'un argument est bien passé
if len(sys.argv) > 1:
    f = factorial(int(sys.argv[1]))
    print(f)
else:
    print("Usage: ./script.py <nombre>")
    