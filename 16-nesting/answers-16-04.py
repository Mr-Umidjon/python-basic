# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 20:57:13 2021

@author: WINDOWS 10
"""

# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida
# ma'lumotlarni lug'at ko'rinishda saqlang. Har bir davlat haqida ma'lumotlarni 
# konsolga chiqaring.


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
for davlat, info in davlatlar.items():
    if davlat.lower()=='aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}\n"
          f"Hududi: {info['hudud']} kv.km\nAholisi: {info['aholi']}\
              \nPul birligi: {info['pul_birlig']}")