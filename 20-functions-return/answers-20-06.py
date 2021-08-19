# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:32:53 2021

@author: WINDOWS 10
"""

# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi 
# ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing. 
# Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng 
# bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ich
# had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,.
def fibonachchi(son):
    fibonach = []
    for x in range(son):
        if x == 0 or x == 1:
            fibonach.append(1)
        else:
            fibonach.append(fibonach[x-1]+fibonach[x-2])
    return fibonach