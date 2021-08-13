# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:18:46 2021

@author: WINDOWS 10
"""

# Taomlar degan ro'yxat yarating va istalgan 5 ta taomni kiriting.
taomlar = ['osh', 'manti', 'kabob', 'saryog\'', "qaymoq"]

# Nonushta degan yangi ro'yxatga taomlardan nusxa oling.
nonushta = taomlar[:]

# Yangi ro'yxatta faqat nonushtaga yeyiladigan taomlarni qoldiring 
# va qo'shimcha 2 ta taom qo'shing.
del nonushta[1]
nonushta.remove("osh")
nonushta.remove("kabob")

nonushta.append('yogurt')
nonushta.insert(1, "kalbasa")

# Ikka ro'yxatni ham konsolga chiqaring.
print(taomlar)
print(nonushta)