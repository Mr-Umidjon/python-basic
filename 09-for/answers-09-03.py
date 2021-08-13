# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 18:53:07 2021

@author: WINDOWS 10
"""

# Foydalanuvchidan bugun nechta odam bilan uchrashganini so'rang va 
# har bir suhbatlashgan odamini ismini birma bir so'rab ro'yxatga yozing.
# Ro'yxatni konsolga chiqaring.
n = int(input("Bugun necha kishi bilan suhbat qildingiz  "))
odamlar = []
for i in range(n):
    odamlar.append(input(f"{i+1}-suhbat qilgan odamingiz kim edi. "))
print(odamlar)