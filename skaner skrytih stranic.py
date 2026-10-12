import requests

file = open("users.txt", "r", encoding="utf-8") #может быть Ваш файл
us = file.read().splitlines()
file.close()

url = input("URL: ")

for d in us:
    full_url = url + d.strip()

    response = requests.get(full_url)

    if response.status_code == 200:
        print(f"Naydena skrytaya stranica: {full_url}")                         