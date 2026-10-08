baza = {
    "user1": "lЫф)4о",
    "admin": " ряVЙТС",
    "user 3": "&кjй&_",
    "rob": "ЮпДяH$"
}

while True:
    a = input("Vvedite login for proverki: ")
    if a in baza:
        print(f"akk scomproment, ego parol: {baza[a]}")
    else:
        print("Vse norm")