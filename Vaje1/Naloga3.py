def PalSito(dat):
    """Prebere datoteko in loči palindrome of nepalindromov, ter oboje vrne kot dve novi datoteki"""
    with open(dat) as datoteka:
        sezpal = []
        seznepal = []
        for line in datoteka:
            oklestena = line.strip(" ")
            for beseda in oklestena:
                jepal = True
                i = 1
                l = len(beseda)
                while i <= l // 2:
                    if beseda(i-1) != beseda(l-i):
                        jepal = False
                    i = i + 1
                if jepal == True:
                    sezpal.append(beseda)
                else:
                    seznepal.append(beseda)
palindromi = "palindromi.txt"
nepalindromi = "nepalindromi.txt"
with open(palindromi, "w") as pal:
    for palindrom in sezpal:
        pal.write(palindrom)

with open(nepalindromi, "w") as nepal:
    for nepalindrom in seznepal:
        nepal.write(nepalindrom)

