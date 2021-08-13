# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:33:29 2021

@author: WINDOWS 10
"""

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, 
# "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?"
# xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"
# matnini konsolga chiqaring.
foydalanuvchi_ismi = input('Foydalanuvchi ismini kiriting ')
if foydalanuvchi_ismi.lower() == 'admin':
    xabar = "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?"
else:
    xabar = f"Xush kelibsiz, {foydalanuvchi_ismi.title()}!"
print(xabar)