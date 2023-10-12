import matrika
# matrika = matrika.Preberi("primer.txt")

def Povezava(mat, v1, v2):
    rez = False
    if mat[v1][v2] == 1:
        rez = True
    return rez
# Povezava je O(1)

#print(Povezava(matrika.Preberi("primer.txt"), 1, 3))
#print(Povezava(matrika.Preberi("primer.txt"), 1, 1))
#print(Povezava(matrika.Preberi("primer.txt"), 1, 5))

def Sosede(mat, v1):
    sosede = []
    for i in range(0, len(mat)):
        if mat[i][v1] == 1:
            sosede.append(i)
    return sosede

#Sosede je O(n)

#print(Sosede(matrika.Preberi("primer.txt"), 0))
#print(Sosede(matrika.Preberi("primer.txt"), 2))
#print(Sosede(matrika.Preberi("primer.txt"), 5))
#print(Sosede(matrika.Preberi("primer.txt"), 3))

def Dodajpovezavo(mat, v1, v2):
    if mat[v1][v2] == 1:
        return "Vozlišči sta že povezani!"
    else:
        mat[v1][v2] = 1
        mat[v2][v1] = 1
        return mat

#DodajPovezavo je O(1)
    
#print(Dodajpovezavo(matrika.Preberi("primer.txt"), 4, 0 ))
    
def Odstranipovezavo(mat, v1, v2):
    if mat[v1][v2] == 1:
        mat[v1][v2] = 0
        mat[v2][v1] = 0
        return mat
    else:
        print("Vozlišči {} in {} nista povezani!".format(v1, v2))

# Odstranipovezavo je O(1)

#print(Odstranipovezavo(matrika.Preberi("primer.txt"), 4, 1 ))
        
def Odstranivsepovezave(mat, v1):
    for i in range(0, len(mat)):
        Odstranipovezavo(dat, v1, i)
    return mat

# Odstranivsepovezave je O(n)

def Izpisivsepovezave(mat):
    povezave = []
    for i in range(0, len(mat)):
        for j in range(0, i):
            if Povezava(mat, i,j) == True:
                povezave.append([i, j])
    return povezave

# Izpisivsepovezave je O(n)

#Izpisivsepovezave(matrika.Preberi("primer.txt"))
