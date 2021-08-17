# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:33:57 2021

@author: WINDOWS 10
"""


# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi 
# har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring 
# (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa
# mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni
# kor'sating.

mahsulotlar = {'sabzi':10000, 'piyoz':1300, 'qlampir':3000, 'banan':23000}
buyurtmalar = []
savol = 'Qanday mahsulot buyurtma berasiz '
while True:
    buyurtma = input(savol)
    buyurtmalar.append(buyurtma)
    javob = input("Yana buyurtma berasizmi (ha/yo'q)")  
    if javob != 'ha':
        break
    
while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar:
        print(f"{buyurtma.title()} ning narhi {mahsulotlar[buyurtma]} so'm ")
    else:
        print(F"Bizda {buyurtma} yo'q ")