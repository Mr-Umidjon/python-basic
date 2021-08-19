# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:30:40 2021

@author: WINDOWS 10
"""

# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, 
# diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya
# yozing
def aylana_info(radius, pi = 3.14159):
    """Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, 
    diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
    diametr = 2 * radius
    perimetr = 2 * pi * radius
    yuza = pi * radius**2
    aylana = {
        "radius": radius,
        "diametr": diametr,
        "perimetr": perimetr,
        "yuza": yuza
        }
    return aylana

print(aylana_info(100))