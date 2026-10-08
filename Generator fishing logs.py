import random

n = int(input("Количество пользователей: "))
users = [0] * n
for i in range (n):
    users[i] = input("Введите пользователя: ")

symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+№;%:?*абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def pasw(par):
    itog = ""
    for i in range(par):
        itog += random.choice(symbols)
    return itog


for i in range(n):
    gotov = pasw(6)
    print(f"User: {users[i]}, Pass: {gotov}")
print(f"Vsego people vzlom: {len(users)}")