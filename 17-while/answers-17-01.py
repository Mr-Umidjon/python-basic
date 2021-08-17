# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:31:29 2021

@author: WINDOWS 10
"""

# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritshni so'rang. Foydalanuvchi
# stop so'zini yozishi bilan dasturni to'xtating.
kitoblar = []
while True:
    kitob = input("Kitob nomini kiriting. (Barcha kitoblarni kiritib bo'lgach 'stop' deb yozing) " )
    if kitob.lower() == 'stop':
        break
    else:
        kitoblar.append(kitob)