# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:25:59 2021

@author: WINDOWS 10
"""

# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing
# ro'yxat elementlarining birinchi harfni katta qilib konsolga chiqaring.
# GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())     
    else:
        print(car.title())
print("\n")
        
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
for car in cars:
    if car != "gm":
        print(car.title())
    else:
        print(car.upper())
        