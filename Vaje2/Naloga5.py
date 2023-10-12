import Naloga4
Testni = Naloga4.Preberivsez("primer.txt")

def Povezava(sez, v1, v2):
    rez = False
    if v1 in sez[1][v2] or v2 in sez[1][v1]:
        rez = True
    return rez

#Zahtevnost Povezava je O(1)

#Povezava(Testni, 1, 3)
#Povezava(Testni, 1, 1)
#Povezava(Testni, 1, 5)

def Sosede(sez, v1):
    return sez[1][v1]

#Zahtevnost Sosede je O(1)

#print(Sosede(Testni, 0))
#print(Sosede(Testni, 2))
#print(Sosede(Testni, 5))
#print(Sosede(Testni, 3))

def Dodajpovezavo(sez, v1, v2):
    sez[1][v1].append(v2)
    sez[1][v2].append(v1)
    sez[1][v1].sort()
    sez[1][v2].sort()
    vm = min(v1, v2)
    vM = max(v1, v2)
    for vi in range(vm+1, len(sez[0])):
        sez[0][vi] += 1
    for vj in range(vM+1, len(sez[0])):
        sez[0][vj] += 1
    return sez

# Zahtevnost Dodajpovezavo je O(n)

#print(Testni)
#print(Dodajpovezavo(Testni, 4, 0 ))

def Odstranipovezavo(sez, v1, v2):
    vm = min(v1, v2)
    vM = max(v1, v2)
    if v1 in sez[1][v2]: #potem je avtomatsko tudi v2 in sez[1][v1]
        sez[1][v2].remove(v1)
        sez[1][v1].remove(v2)
        for vi in range(vm+1, len(sez[0])):
            sez[0][vi] -= 1
        for vj in range(vM+1, len(sez[0])):
            sez[0][vj] -= 1
        return sez
    else:
        print("Vozlišči {} in {} nista povezani!".format(v1, v2))

# Zahtevnost Odstranipovezavo je O(n)

#print(Odstranipovezavo("primer.txt", 4, 1 ))

def Odstranivsepovezave(sez, v1):
    sos = sez[1][v1]
    for i in sos:
        Odstranipovezavo(sez, v1, i)
    return sez

# Zahtevnost Odstranivsepovezave je O(n)

def Izpisivsepovezave(sez):
    povezave = []
    n = len(sez[0])
    for i in range(n):
        for j in range(i):
            if Povezava(sez, i,j) == True:
                povezave.append([i, j])
    return povezave
#Izpisivsepovezave(matrika)
