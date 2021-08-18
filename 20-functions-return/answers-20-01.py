# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 15:23:02 2021

@author: WINDOWS 10
"""


def oraliq(min, max, qadam=1):
    "range funksiyasinig odidiy varianiti"
    sonlar = []
    while min < max:
        sonlar.append(min)
        min = min + qadam
    return sonlar