# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:31:57 2021

@author: WINDOWS 10
"""


# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
# (tub sonlar — faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
def tub_son(a, b):
    """Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya"""
    tub_sonlar = []
    for son in range(a, b+1):
        tub = True
        if son == 1:
            tub = False
        elif son == 2:
            tub = True
        else:
            for x in range(2, son):
                if son%x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(son)
    return tub_sonlar