# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 15:01:21 2021

@author: WINDOWS 10
"""

# Restoran menusi lug'atini tuzing va foydalanuvchidan 3 ta ovqat buyurtma 
# berishini so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring
# agar taom menuda bo'lsa narhini ko'rsating, aks holda "Bizda bunday taom yo'q"
# degan xabarni chiqaring.
menu = {'osh':14000, 'dimlama':18000, 'bishteks':12, "lag'mon":15000,
        'kabob':10000, 'manti':2500, 'choy':1000, 'kofe':2000, 'kola':5000}
buyurtmalar = []

print('3 ta taom buyurtma bering ')
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom ").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm ")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q")
        