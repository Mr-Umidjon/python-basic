# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:19:31 2021

@author: WINDOWS 10
"""

# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi
# juft son kiritsa "Rahmat", agar toq son kiritsa "Bu son juft emas"
# degan xabarni chiqaring.
son = int(input("Juft son kiriting "))
if son % 2 == 0:
    print("Rahmat")
else:
    print("Bu son juft emas")