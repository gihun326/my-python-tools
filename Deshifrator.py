alfabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
def deshifrator(tayna):
        itog = ""
        for bukva in tayna:
            if bukva in alfabet:
                ind = alfabet.index(bukva)
                novaya_bukovka = alfabet[(ind - sdvig) % len(alfabet)]
                itog += novaya_bukovka
            else:
                itog += bukva
        return itog

vvod = input("Tekst dlya deshifry: ").lower()
sdvig = int(input("Vvedite shag(chislo): "))
slovo = deshifrator(vvod)
print(f"Zashifr: {slovo}")
