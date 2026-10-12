import requests

url = input("URL sayta: ")

response = requests.get(url)

if response.status_code == 200:
    print("Sayt rabotaet!")
else:
    print(f"Sayt ne otvechaet. Kod oshibki: {response.status_code}")