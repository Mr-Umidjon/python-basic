# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 21:19:11 2021

@author: WINDOWS 10
"""

# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas,
# foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning
# lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan
# xabarni konsolga chiqaring.

davlatlar = {
    "o'zbekiston":{
        'poytaxt':'toshkent',
        'hudud':448978,
        'aholi':33000000,
        'pul_birlig':"so'm"
        },
    'rossiya':{
        'poytaxt':'maskva',
        'hudud':17098246,
        'aholi':144000000,
        'pul_birlig':'rubl'
        },
    'aqsh':{
        'poytaxt':'vashington',
        'hudud':9631418,
        'aholi':327000000,
        'pul_birlig':'dollor'
        }
    }
davlat = input('Davlat nomini kiriting: ').lower()

if davlat in davlatlar:
    info = davlatlar[davlat]
    if davlat.lower()=='aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}\n"
          f"Hududi: {info['hudud']} kv.km\nAholisi: {info['aholi']}\
              \nPul birligi: {info['pul_birlig']}")
else:
    print(f"Bizda {davlat.title()} haqida ma'lumot yo'q")
    
    
    
    
    