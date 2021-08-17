# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:43:40 2021

@author: WINDOWS 10
"""

# Muzeyda chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan
# yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 
# 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi
# yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit
# deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
# Yuqoridagi dasturni turli usullarda yozib ko'ring
# (break, ishora, yoki shart tekshirish)


# ishora = True
# while ishora:
#     age = input("Yoshingizni kiriting (chiqish uchun exit deb yozing) ")
#     if age == 'exit':
#         ishora = False
#     else:
#         age = int(age)
#         if age < 7:
#             narh = 2000
#         elif age < 18:
#             narh = 3000
#         elif age < 65:
#             narh = 10000
#         else:
#             narh = 0
#         print(f"Sizga kirish {narh} so'm") 

while True:
    age = input("Yoshingizni kiriting (chiqish uchun exit yoki quit deb yozing) ")
    if age == 'exit' or age == 'quit':
        break
    age = int(age)
    if age < 7:
        narh = 2000
    elif age < 18:
        narh = 3000
    elif age < 65:
        narh = 10000
    else:
        narh = 0
    if narh == 0:
        print("Sizga kirish bepul ")
    else:
        print(f"Sizga kirish {narh} so'm")