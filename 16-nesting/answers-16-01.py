# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 19:46:39 2021

@author: WINDOWS 10
"""


# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxslar
# haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta 
# ro'yxatga joylang va har bir shaxs haqida ma'lumotlarni konsolga
# chiqaring.
buxoriy = {'ism':"Abu Abdulloh Muhammad ibn Ismoil", 'tyil':810, 'umr':60, "tjoy":"Buxoro"}
qodiriy = {'ism':"Abdulla Qodiriy", 'tyil':1894, 'umr':44, "tjoy":"Toshkent"}
vohidov = {'ism':"Erkin Vohidov", 'tyil':1936, 'umr':80, "tjoy":"Farg'ona"}
navoiy = {'ism':"Alisher Navoiy", 'tyil':1441, 'umr':60, "tjoy":"Hirot"}
shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
for shaxs in shaxslar:
    ism = shaxs['ism']
    tyil = shaxs['tyil']
    tjoy = shaxs['tjoy']
    umr = shaxs['umr']
    print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan.\
   {umr} yil umr ko'rgan")
   