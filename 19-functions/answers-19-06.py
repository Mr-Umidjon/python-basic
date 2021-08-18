# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 14:31:18 2021

@author: WINDOWS 10
"""

# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga 
# qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga
# chiqaring.
def bolinish_alomatlari(son):
    """2 dan 10 gacha bo'lgan sonlarga bo'linish alomatlarini tekshiruvchi funksiya"""
    for x in range(2, 10):
        if son%x == 0:
            print(f"{son} soni {x} ga qoldiqsiz bo'linadi. ")
bolinish_alomatlari(21)
bolinish_alomatlari(900)