# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:56:21 2021

@author: WINDOWS 10
"""

# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi
# harfini katta harfga o'zgatiruvchi funksiya yozing. 
def katta_harf(matnlar):
    """Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning
    birinchi harfini katta harfga o'zgatiruvchi funksiya"""
    k_matnlar = []
    for matn in matnlar:
        k_matnlar.append(matn.capitalize())
    print(k_matnlar)
ismlar = ['ali', 'vali', 'hasan', 'husan']

katta_harf(ismlar)
print(ismlar)

# Kutilgan natija: ['Ali', 'Vali', 'Hasan', 'Husan']

# Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat 
# qaytaradigan qilib o'zgartiring
def katta_harf(matnlar):
    """Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning
    birinchi harfini katta harfga o'zgatiruvchi funksiya"""
    k_matnlar = []
    for matn in matnlar:
        k_matnlar.append(matn.capitalize())
    return k_matnlar
ismlar = ['ali', 'vali', 'hasan', 'husan']

yangi_ismlar = katta_harf(ismlar)

print(ismlar)

print(yangi_ismlar)

# Kutilgan natija: 

# ['ali', 'vali', 'hasan', 'husan'] 

# ['Ali', 'Vali', 'Hasan', 'Husan']

# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan 
# foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at 
# qaytaradigan qilib yozing.