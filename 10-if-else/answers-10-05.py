# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:51:31 2021

@author: WINDOWS 10
"""

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa, uning 
# ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, 
# "Musbat son kiriting" degan xabarni chiqaring.
son = float(input("Istalgan son kiriting "))
if son >= 0:
    print(son**(1/2))
else:
    print("Musbat son kiriting")