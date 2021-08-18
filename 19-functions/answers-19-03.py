# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 14:28:03 2021

@author: WINDOWS 10
"""

# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi 
# funksiya yozing.
def juftmi(son):
    """Sonning juft yoki toqligini hisoblovchi funksiya"""
    if son%2 == 0:
        print(f"{son} juft son")
    else:
        print(f"{son} toq son")
juftmi(23)
juftmi(654)