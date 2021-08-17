# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:33:17 2021

@author: WINDOWS 10
"""

# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi 
# dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar 
# (mahsulot va uning narhi) kiritishni so'rang.

e_bozor = {}
while True:
    kalit = input("Mahsulot nomini kiriting ")
    qiymat = float(input(f"{kalit.title()} ning narhini kiriting "))
    e_bozor[kalit] = qiymat
    javob = input("Yana mahsulot qo'shasizmi (ha/yo'q) ")
    if javob != 'ha':
        break
print(e_bozor)