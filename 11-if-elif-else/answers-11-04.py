# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:37:49 2021

@author: WINDOWS 10
"""

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni 
# kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan
# kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar
# ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda
# bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarni chiqaring.
mahsulotlar = ['olma', 'nok', 'anor', "bexi", 'olcha', 'banan', 'apelsin', 'limon', 'uzum', 'madarin']
savat = []
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni qo'shing "))
    
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot.lower()} bor")
    else:
        print(f"Do'konimizda {mahsulot.lower()} yo'q")