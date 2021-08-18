# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 20:15:19 2021

@author: WINDOWS 10
"""

# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi
# funksiya yozing.
def kvadrat_kub_hisobla(son):
    """Son qabul qilib uning kvadrati va kubini konsolga chiqaruvchi funksiya"""
    print(f"{son} kvadrati: {son**2} ga teng. Kubi: {son**3} ga.")
kvadrat_kub_hisobla(2)
kvadrat_kub_hisobla(21)

# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi 
# funksiya yozing.
def juftmi(son):
    """Sonning juft yoki toqligini hisoblovchi funksiya"""
    if son%2 == 0:
        print(f"{son} juft son")
    else:
        print(f"{son} toq son")
juftmi(23)
juftmi(654)

# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi 
# funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni 
# chiqaring.
def max_son(a, b):
    if a > b:
        print(a)
    elif a < b:
        print(b)
    else:
        print("Sonlar teng ")
max_son(23, 34)
max_son(90, 21)
max_son(9, 9)

# Foydalanuvchidan x va y sonlarini olib, x**y konsolga chiqaruvchi 
# funksiya yozing.
def daraja(x, y):
    """x darajasi y ni hisoblovchi funksiya"""
    print(f"{x} ning {y}-darajasi {x**y} ga teng ")
daraja(9, 2)
daraja(34, 5)


# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
def daraja(x, y=2):
    """x darajasi y ni hisoblovchi funksiya"""
    print(f"{x} ning {y}-darajasi {x**y} ga teng ")
daraja(9)
daraja(34)

# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga 
# qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga
# chiqaring.
def bolinish_alomatlari(son):
    """2 dan 10 gacha bo'lgan sonlarga bo'linish alomatlarini tekshiruvchi funksiya"""
    for x in range(2, 10):
        if son%x == 0:
            print(f"{son} soni {x} ga qoldiqsiz bo'linadi. ")
bolinish_alomatlari(21)
bolinish_alomatlari(900)




