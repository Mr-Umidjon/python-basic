# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 21:48:55 2021

@author: WINDOWS 10
"""

# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning 
# xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan 
# ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)
class User:
    def __init__(self, ism, foydalanuvchi_ismi, email, telefon):
        self.ism = ism
        self.foydalanuvchi_ismi = foydalanuvchi_ismi
        self.email = email
        self.telefon = telefon
        
# Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi
# haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan: 
# "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).
    def get_info(self):
        info = f"Foydalanuvchi: {self.foydalanuvchi_ismi}, ismi: {self.ism.title()}, email: {self.email}, telefon: {self.telefon}."
        return info
    
# Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga
# murojat qiling.
user1 = User("Umidjon Maxammadsoliyev", "Mr Umidjon", "mrumidjon2020@gmail.com", 900223538)
user2 = User("Odiljon", "Odiljonboy", "odiljonboy@gmail.com", 331559049)
print(user2.ism)
print(user1.get_info())