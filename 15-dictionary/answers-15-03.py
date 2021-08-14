# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 14:49:01 2021

@author: WINDOWS 10
"""

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning 
# poytaxtni konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlat kiritsa
# "Bizda bunday ma'lumot yo'q" degan xabarni konsolga chiqaring.
davlatlar = {'uzbekistan':'tashkent',
             'aqsh':'washington',
             'italiya':'rim',
             'malayziya':'kuala-lumpur',
             'rossiya':'maskava',
             'kanada':"toronto"}

davlat = input("Qaysi davlatning poytaxtni bilishni istaysiz: ").lower()
poytaxt = davlatlar.get(davlat)

if poytaxt == None:
    print("Bizda bunday ma'lumot yo'q")
else:
    print(f"{davlat.upper()}ning poytaxti {davlatlar[davlat].title()} shahri")
    