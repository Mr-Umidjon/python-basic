# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 14:26:47 2021

@author: WINDOWS 10
"""

# Python izohli lug'ati tuzing: Lug'atga shu kungacha o'rgangan 10 ta so'z 
# kiriting. Lug'atdagi har bir kalit va qiymatni for tskili yordamida, alifbo
# ketma-ketligida chiqoyli qilib konsolga chiqaring.
izohli_lugat = {'integer':'butun son', 'float':"o'nlik son", 'string':'matn turi',
                'if':"agar shart operatori", 'boolean':'mantiqiy toifa',
                'true':'rost qiymat', 'false':"yolg'on qiymat", "list":"ro'yxat",
                'input':'kiritish oqimi', "print":"chop qilish"}

for kalit, qiymat in sorted(izohli_lugat.items()):
     print(f"{kalit.title()} - {qiymat.capitalize()}")