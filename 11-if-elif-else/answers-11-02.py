# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:24:42 2021

@author: WINDOWS 10
"""

# Foydalanuvchidan yoshini so'rang va muzeyga kirish narhini quyidagicha chiqaring:
#  Agar foydalanuvchi 4 yoshdan kichik va 60 yoshdan katta bo'lsa bepul
#  Agar foydalanuvchi 18 yoshdan kichik bo'lsa 10000 so'm
#  Agar foydalanuvchi 18 yoshdan katta bo'lsa 20000 so'm

yosh = int(input("Yoshingiz nechchida? "))
if yosh < 4 or yosh > 60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Sizga kirish {narh} so'm")