par = input("Vvedite vash parol: ")

1 = False
2 = False
for symvol in par:
    if symvol.isdigit():
        1 = True
    if symvol.isupper():
        2 = True
if len(par) >= 8 and 1 == True and 2 == True:
    print("Norm")
else:
    print("Ne podhodit.")