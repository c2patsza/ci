import unittest
def abs_max():
    a = abs(int(input('Input: ')))
    b = abs(int(input(', ')))
    if a > b:
        return a
    elif b > a:
        return b
print(abs_max())