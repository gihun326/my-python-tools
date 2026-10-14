import requests

file = open("users.txt", "r", encoding="utf-8") #может быть Ваш файл
us = file.read().splitlines()
file.close()

file = open("sayti.txt", "r", encoding="utf-8") 
sy = file.read().splitlines()
file.close()


while True:
    for s in sy:
        url = s.strip()
        for d in us:
            full_url = url + d.strip()
            try:
                response = requests.get(full_url)
                if response.status_code == 200:
                    print(f"Naydena skrytaya stranica: {full_url}")
            except:
                pass
    break
