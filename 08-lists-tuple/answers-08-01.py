# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 14:27:45 2021

@author: WINDOWS 10
"""

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
countries = ['Uzbekistan', 'USA', "Kanada", "Japon", "China", "India"]
print(countries)

# Ro'yxating uzunligini konsolga chiqaring.
l = len(countries)
print(l)

# sorted() funksiyasi yordamida ro'yxatni tartiblangan holatda konsolga chiqaring.
print(sorted(countries))

# sorted() funksiyasi yordamida ro'yxatni teskari tartiblangan holatda konsolga chiqaring.
print(sorted(countries, reverse=True))

# Asil ro'yxatni qaytadan konsolga chiqaring.
print(countries)

# reverse() funksiyasi yordamida ro'yxatni ortidan boshlab chiqaring.
countries.reverse()
print(countries)

# sort() metodi yordamida avval ro'yxatni alifbo bo'yicha, keyin esa alifboga
# teskari tartibda konsolga chiqaring.
countries.sort()
print(countries)

countries.sort(reverse=True)
print(countries)