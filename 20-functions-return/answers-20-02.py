# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 14:32:19 2021

@author: WINDOWS 10
"""

# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
# email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
# qaytaruvchi funksiya yozing. Lug'atda foydalanuvchining yoshi ham bo'lsin. 
# Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
def user_info(ism, familiya, tyil, tjoy, yosh, email=None, telefon=None):
    info = {'ism':ism,
            "familiya":familiya,
            "tyil":tyil,
            'tjoy':tjoy,
            "yosh":yosh ,
            'email':email,
            "telefon":telefon       
        }
    return info
user = user_info("ali", "valiyev", 1987, "andijon", 23)

# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar
# degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni
# konsolga chiqaring.
mijozlar = []
# while True:
#     print("\nMijoz haqida quyidagi ma'lumotlarni kiriting ")
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili:"))
#     tjoy = input("Tug'ilgan joyi: ")
#     yosh = int(input("Yoshi: "))
#     email = input("Email manzili: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(user_info(ism, familiya, tyil, tjoy, yosh, email, telefon))
#     javob = input("Yana mijoz haqida ma'lumot kiritasizmi(yes/no)")
#     if javob == 'no':
#         break
# for mijoz in mijozlar:
#     info = f"{mijoz['ism'].title()} {mijoz['familiya'].title()} "
#     info += f"{mijoz['tyil']}-yilda {mijoz['tjoy'].title()}da tug'ilgan. "


# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
def max_top(a, b, c):
    """Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya"""
    if a > b and a > c:
        max = a
    elif b > a and b > a:
        max = b
    else:
        max = c
    return max

# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, 
# diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya
# yozing
def aylana(radius):
    """Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, 
    diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
    diametr = 2 * radius
    perimetr = 2 * 3.14 * radius
    yuza = 3.14 * radius**2
    aylana = {
        "radius": radius,
        "diametr": diametr,
        "perimetr": perimetr,
        "yuza": yuza
        }
    return aylana
    

# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)

# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing. Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,.