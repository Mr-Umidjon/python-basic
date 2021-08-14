# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 14:36:03 2021

@author: WINDOWS 10
"""

# Davlatlar va ularning poytxatlari lug'atini tuzing. Avval lug'atdagi
# davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida 
# konsolga chiqaring.
davlatlar = {'uzbekistan':'tashkent',
             'aqsh':'washington',
             'italiya':'rim',
             'malayziya':'kuala-lumpur',
             'rossiya':'maskava',
             'kanada':"toronto"}

print("Dunyo davlatlari: ")
for davlat in sorted(davlatlar):
    print(davlat.upper())

print("\nDavlatlarning poytaxtlari: ")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())
    