# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:31:23 2021

@author: WINDOWS 10
"""

# Foydalanuvchidan ikkita son kiritishni so'rang, sonlarni solishtiring va
# ularning teng yoki katta/kichik ligi haqida xabar chiqaring.
a = float(input("Birinchi sonni kiriting "))
b = float(input("Ikkinchi sonni kiriting "))
if a > b:
    print(f"{a} > {b}")
elif a < b:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")