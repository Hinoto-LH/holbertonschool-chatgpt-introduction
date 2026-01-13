#!/usr/bin/python3
import sys
#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1   # ← correction essentielle
    return result

if len(sys.argv) != 2:
    print("Usage: ./factorial.py <nombre>")
    sys.exit(1)

f = factorial(int(sys.argv[1]))
print(f)