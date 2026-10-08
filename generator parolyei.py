import random

symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+№;%:?*абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def pasw(par):
    itog = ""
    for i in range(par):
        itog += random.choice(symbols)
    return itog

dlin_par = int(input("Kol-vo simv: "))
gotov = pasw(dlin_par)
print(f"Vash parol: {gotov}")
