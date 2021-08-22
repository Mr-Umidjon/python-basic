# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 07:47:54 2021

@author: WINDOWS 10
"""


# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi
# funksiya yozing
def multiply(*sonlar):
    """Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi 
    funksiya"""
    kopaytma = 1
    for son in sonlar:
        kopaytma = kopaytma * son
    return kopaytma
print(multiply(6, 3, 2))
print(multiply(6, 7, 9, 20, 2, 1))
