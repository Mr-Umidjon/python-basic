# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:47:25 2021

@author: WINDOWS 10
"""

# Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy 
# holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
savol = "Kiritilgan sonni ildizini qayaruvchi dastur. "
savol += "Musbat son kiriting "
savol += "(Dasturni to'xtatish uchun 'exit' deb yozing) "
while True:
    qiymat = input(savol)
    if qiymat == "exit":
        break
    elif float(qiymat) < 0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng ")