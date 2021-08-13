# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:08:20 2021

@author: WINDOWS 10
"""

# Python izohli lug'ati tuzing: Lug'atga shu kungacha o'rgangan 10 ta so'z 
# kiriting va har birining qisqacha tarjimasini yozing.
izohli_lugat = {'integer':'butun son', 'float':"o'nlik son", 'string':'matn turi',
                'if':"agar shart operatori", 'boolean':'mantiqiy toifa',
                'True':'rost qiymat', 'False':"yolg'on qiymat", "list":"ro'yxat",
                'input':'kiritish oqimi', "print":"chop qilish"}

# Foydalanuvchidan biror so'z kiritshni so'rang va so'zning tarjimasini
# yuqoridagi lug'atdan chiqarib bering. Agar so'z lug'atda mavjud bo'lmasa,
# "Bunday so'z mavjud emas" degan xabarni chiqaring.
key = input("Kalit so'zni kiriting: ").lower()
print(izohli_lugat.get(key, "Bunday so'z mavjud emas"))

# Yuqoridagi vazifani if else yordamida qiling va natijani foydalanuvchiga 
# tushunarli ko'rinishda chiqaring.
if key in izohli_lugat.keys():
    print(f"{key.title()} so'zi {izohli_lugat[key].capitalize()} deb tarjima qilinadi.")
else:
    print("Bunday so'z mavjud emas ")