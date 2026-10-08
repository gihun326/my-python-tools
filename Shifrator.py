alfabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
def shifrator(ishod):
    itog = ""
    for bukva in ishod:
        if bukva in alfabet:
            ind = alfabet.index(bukva)
            novaya_bukovka = alfabet[(ind + sdvig) % len(alfabet)]
            itog += novaya_bukovka
        else:
            itog += bukva
    return itog

vvod = input("Tekst dlya shifry: ").lower()
sdvig = int(input("Vvedite shag(chislo): "))
slovo = shifrator(vvod)
print(f"Zashifr: {slovo}")
