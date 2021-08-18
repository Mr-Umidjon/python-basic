# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 14:28:52 2021

@author: WINDOWS 10
"""

# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi 
# funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni 
# chiqaring.
def max_son(a, b):
    if a > b:
        print(a)
    elif a < b:
        print(b)
    else:
        print("Sonlar teng ")
max_son(23, 34)
max_son(90, 21)
max_son(9, 9)