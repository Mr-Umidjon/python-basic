# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 13:53:42 2021

@author: WINDOWS 10
"""

# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya
# yozing. Talabaning ismi va familiyasi majburiy argument, qolgan
# ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
def talaba_info(ism, familiya, **malumotlar):
    """Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya """
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar