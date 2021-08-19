# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 14:32:19 2021

@author: WINDOWS 10
"""

# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
# email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
# qaytaruvchi funksiya yozing. Lug'atda foydalanuvchining yoshi ham bo'lsin. 
# Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
def mijoz_info(ism, familiya, tyil, tjoy, yosh, email='', telefon=None):
    info = {'ism':ism,
            "familiya":familiya,
            "tyil":tyil,
            'tjoy':tjoy,
            "yosh":yosh ,
            'email':email,
            "telefon":telefon       
            }
    return info
user = mijoz_info("ali", "valiyev", 1987, "andijon", 23)

# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar
# degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni
# konsolga chiqaring.
mijozlar = []
print("\nMijoz haqida quyidagi ma'lumotlarni kiriting ")
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili:"))
    tjoy = input("Tug'ilgan joyi: ")
    yosh = int(input("Yoshi: "))
    email = input("Email manzili: ")
    telefon = input("Telefon raqami: ")
    mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, yosh, email, telefon))
    javob = input("Yana mijoz haqida ma'lumot kiritasizmi(yes/no)")
    if javob == 'no':
        break
print('\nMijozlar: ')
for mijoz in mijozlar:
    info = f"{mijoz['ism'].title()} {mijoz['familiya'].title()} "
    info += f"{mijoz['tyil']}-yilda {mijoz['tjoy'].title()}da tug'ilgan. "

        
