# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:28:23 2021

@author: WINDOWS 10
"""

# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
def max_top(a, b, c):
    """Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya"""
    if a >= b and a >= c:
        max = a
    elif b >= a and b >= c:
        max = b
    else:
        max = c
    return max
print(max_top(23, 4356, 567))
print(max_top(32456, 67, 879))
print(max_top(90, 98, 89765))


def kattasi(x, y, z):
    max = x
    if y >= max:
        max = y
    if z >= max:
        max = z
    return max
print(9, 9, 17)   