# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:19:54 2021

@author: WINDOWS 10
"""

# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan 
# foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at 
# qaytaradigan qilib yozing.
def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baholar[ism] = int(input(f"Talaba {ism.title()}ning bahosini kiriting: "))
    return baholar