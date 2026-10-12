file = open("password.txt", "w", encoding="utf-8")
file.write('123456 \n' )
file.write('12345678 \n' )
file.write('00000000 \n' )
file.write('123456789 \n' )
file.write('11111111 \n')
file.close()
# по хорошему этот блок снести надо, для реальной работы.

file = open("password.txt", "r", encoding="utf-8")
passw = file.read().splitlines()
file.close()

secret_passw = "123456789"

for p in passw:

    if p.strip() == secret_passw:
        print(f"Parol vzloman, eto bil: {secret_passw}")
        break
    else:
        print("Net. Esche raz")