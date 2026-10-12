file = open("compromised.txt", "w", encoding="utf-8")
file.write('Panterka \n' )
file.write('admin \n' )
file.write('hacker \n' )
file.write('user1 \n' )
file.write('3000 \n')
file.close()

file = open("compromised.txt", "r", encoding="utf-8")
users = file.read().splitlines()
file.close()

while True:
    a = input("Vvedite login for proverki: ")
    if a in users:
        print("Akk nayden v baze")
    else:
        print("Vse norm")