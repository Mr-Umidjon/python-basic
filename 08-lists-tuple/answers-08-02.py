# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 14:49:17 2021

@author: WINDOWS 10
"""



# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing.
juft_sonlar = list(range(120, 1201, 2))

## Ro'yxatdagi sonlar yig'indisini hisoblang va  konsolga chiqaring
# summa = sum(juft_sonlar)
summa = 0
for son in juft_sonlar:
    summa = summa + son  
print(summa)

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayrimani hisoblang va konsolga chiqaring.
min_son = min(juft_sonlar)
max_son = max(juft_sonlar)
ayrima = max_son - min_son
print(ayrima)

# Ro'yxatdagi elementlar sonini hisoblang.
l = len(juft_sonlar)

# Ro'yxatni boshidan, oxiridan va o'rtasidan konsolga 20 ta qiymatni chiqaring.
bottom = juft_sonlar[:20]
top = juft_sonlar[-20:]
a = l//2 - 10
b = l//2 + 10
center = juft_sonlar[a:b]
