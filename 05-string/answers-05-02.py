# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 09:02:47 2021

@author: WINDOWS 10
"""

# Ko'cha, mahalla, tuman va viloyatini foydalanuvchidan so'rang va quiyidagi ko'rinishda konsolga chiqaring
# namuna: Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati.
kocha = input("Ko'changiz nomini kiriting. ").title()
mahalla = input("Mahallangiz  nomini kiriting. ").title()
tuman = input("Tumaningiz nomini kiriting. ").title()
viloyat = input("Viloyatingiz nomini kiriting. ").title()

print()

# Yuqoridagi matnni chiqarishda har bir verguldan keyin yangi qatorga yozing.
print(f"\n{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati.")

# Yuqoridagi matnni f-string yordamida manzil degan yangi o'zgaruvchiga yuklang.
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati."

# manzil o'zgaruvchiga title(), upper(), lower(), capitalize() metodlarini qo'llab ko'ring.
manzil = manzil.title()
print(manzil)
manzil = manzil.upper()
print(manzil)
manzil = manzil.lower()
print(manzil)
manzil = manzil.capitalize()
print(manzil)