# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 18:53:06 2021

@author: WINDOWS 10
"""

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot
# kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni
# yangi bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa
# mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa
# "Siz so'ragan barcha mahsulotlar do'konimzda bor" degan xabarni, aks holda
# esa "Quyidagi mahsulotlar do'konimizda yo'q:..." degan xabarni chiqaring.
mahsulotlar = ['olma', 'nok', 'anor', "bexi", 'olcha', 'banan', 'apelsin', 'limon', 'uzum', 'madarin']
savat = []
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni qo'shing "))
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
    print("Quyidagi mahsulotlar do'konimizda yo'q:...")
    for mahsulot in mavjud_emas:
        print(mahsulot) 
else:
    print("Siz so'ragan barcha mahsulotlar do'konimzda bor")