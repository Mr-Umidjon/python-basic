# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 19:22:51 2021

@author: WINDOWS 10
"""


# Foydalanuvchilar degan ro'yxat tuzing va kamida 5 ta login qo'shing. 
# Foydalanuvchidan yangi login tanlshni so'rang va foydalnuvchi kiritgan
# loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang"
# aks holda "Xush kelibsiz foydalanuvchi!" xabarini chiqaring.
foydalanuvchilar = ['ali', 'vali', 'akbar', 'botir', 'hasan', 'husan', 'alisher']
login = input("Yangi login tanlang: ")
if login.lower() not in foydalanuvchilar:
    print("Xush kelibsiz foydalanuvchi ")
else:
    print("Login band, yangi login tanlang")
