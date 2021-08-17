# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 20:11:46 2021

@author: WINDOWS 10
"""

# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
# For tsikli yordamida muallifning ismi va asarlarini konsolga chiqaring.

shaxs0 = {'ism':"Abu Abdulloh Muhammad ibn Ismoil", 'tyil':810, 'umr':60, "tjoy":"Buxoro",
          'asarlar':['Al-jome as-sahih', 'Al-adab al-mufrad', 'At-tarix al-kabir', 'At-tarix as asg\'ir']}
shaxs1 = {'ism':"Abdulla Qodiriy", 'tyil':1894, 'umr':44, "tjoy":"Toshkent",
          'asarlar':["O'tkan kunlar", "Merobdan Chayon", "Obid krtmon"]}
shaxs2 = {'ism':"Erkin Vohidov", 'tyil':1936, 'umr':80, "tjoy":"Farg'ona",
          'asarlar':['Tong nafasi', "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"]}
shaxs3 = {'ism':"Alisher Navoiy", 'tyil':1441, 'umr':60, "tjoy":"Hirot",
          'asarlar':['Xamsa', "Lison-ut-Tayr", "Maqbub Al-Qulub", "Munojat"]}
shaxslar = [shaxs0, shaxs1, shaxs2, shaxs3]
for shaxs in shaxslar:
    ism = shaxs['ism']
    asarlar = shaxs['asarlar']
    print(f"\n{ism}ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar)