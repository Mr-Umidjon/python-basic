# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:32:47 2021

@author: WINDOWS 10
"""


# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

buyurtmalar = []
savol = 'Qanday taom buyurtma berasiz '
while True:
    buyurtma = input(savol)
    buyurtmalar.append(buyurtma)
    javob = input("Yana buyurtma berasizmi (ha/yo'q)")  
    if javob != 'ha':
        break
print(buyurtmalar)    