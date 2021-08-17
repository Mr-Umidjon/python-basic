# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 20:31:28 2021

@author: WINDOWS 10
"""

# Olia a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino seriali haqida so'rang.
# Do'stingiz ismi kalit, uning sevimli kinolari esa ro'yxat ko'rinishida lug'atga 
# saqlang. Natijani konsolga chiqaring.
kinolar = {
    'ali':['halk', 'supermen', 'tor', 'uzuklar hukumdori'],
    'vali':['kapitan amerika', 'venom', 'akvamen'],
    'sobir':['qasoskorlar', 'muzyurak', 'qorbobo', 'mehmonxona']
    }

for ism, kinolar in kinolar.items():
    print(f'\n{ism.title()}ning sevimli kinolari: ')
    for kino in kinolar:
        print(kino.title())