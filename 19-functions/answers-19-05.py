# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 14:29:36 2021

@author: WINDOWS 10
"""

# Foydalanuvchidan x va y sonlarini olib, x**y konsolga chiqaruvchi 
# funksiya yozing.
def daraja(x, y):
    """x darajasi y ni hisoblovchi funksiya"""
    print(f"{x} ning {y}-darajasi {x**y} ga teng ")
daraja(9, 2)
daraja(34, 5)


# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
def daraja(x, y=2):
    """x darajasi y ni hisoblovchi funksiya"""
    print(f"{x} ning {y}-darajasi {x**y} ga teng ")
daraja(9)
daraja(34)