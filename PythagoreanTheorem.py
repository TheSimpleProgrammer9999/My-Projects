import math

def formula(a, b):
    a_b = a**2 + b**2
    result = round(math.sqrt(a_b), 2)
    print(result)

a = int(input("Opposite length: "))
b = int(input("Adjacent length: "))

formula(a, b)