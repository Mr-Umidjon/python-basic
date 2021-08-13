# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 19:30:31 2021

@author: WINDOWS 10
"""


# Foydalanuvchidan biror butun son kiritshni so'rang. Foydalanuvchi kiritgan
# sonni 2 dan 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini 
# konsolga chiqaring.
son = int(input("Istalgan butun son kiriting: "))
for n in range(2, 11):
   if son % n == 0:
       print(f"{son} soni {n} ga qoldiqsiz bo'linadi. ")