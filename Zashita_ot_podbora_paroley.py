correct_pass = "1230987"
popytki = 3
for parol in range(3):
    a = input("Введите пароль: ")
    popytki = popytki - 1
    if a != correct_pass:
        print(f"Неправильный пароль. Осталось {popytki} попытка/и.")
    elif a == correct_pass:
        print("Угадал!")
        break
if a != correct_pass:
    print("Не угадал...")