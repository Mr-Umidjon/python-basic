# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 10:23:19 2021

@author: WINDOWS 10
"""

# friends nomli bosh yangi ro'yxat yarting va unga .append() yordamida mehmonga 
# chaqirmoqchi bo'lgan do'stlaringizni kiriting
friends = []
friends.append("Ali")
friends.append("Vali")
friends.append("Hasan")
friends.append("Husan")
friends.append("Akbar")
print(friends)

# Yuqoridagi ro'yxatdan mehmonga kela olmaydingan do'stlaringizni .remove() 
# metodi yordamida o'chirib tashlang
friends.remove("Ali")
friends.remove("Akbar")
print(friends)

# Ro'yxatnig boshi, oxiri va o'rtasiga yangi ismlar qo'shing
friends.insert(0, 'Odiljon')
friends.insert(2, "Umidjon")
friends.insert(5, "Bahramjon")

# Yangi mehmonlar degan bo'sh ro'yxat yarating. .pop() va .append()
# metodlari yordamida friends ro'yxatidan sug'urib olib mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(3))
print(mehmonlar)


