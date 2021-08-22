# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 07:47:54 2021

@author: WINDOWS 10
"""


# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi
# funksiya yozing
def kopaytma(*sonlar):
    """Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi 
    funksiya"""
    s = 1
    for son in sonlar:
        s = s * son
    return s
print(kopaytma(6, 3, 2))
print(kopaytma(6, 7, 9, 20, 2, 1))
