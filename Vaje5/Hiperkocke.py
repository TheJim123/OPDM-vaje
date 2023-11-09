# Vozlišče Hiperkocke dimenzije r predstavimo z nizom 0 in 1 dolžine r
#Pretvori število (prvi argument) v binarni niz dolžine base
#str = "{0:{fill}{base}b}".format(3, base=5, fill="0")
#print(str)


nula = "{0:{fill}{base}b}".format(0, base=3, fill="0")
ena = "{0:{fill}{base}b}".format(1, base=3, fill="0")
dve = "{0:{fill}{base}b}".format(2, base=3, fill="0")
tri = "{0:{fill}{base}b}".format(3, base=3, fill="0")
stiri = "{0:{fill}{base}b}".format(4, base=3, fill="0")
pet = "{0:{fill}{base}b}".format(5, base=3, fill="0")
sest = "{0:{fill}{base}b}".format(6, base=3, fill="0")
sedem= "{0:{fill}{base}b}".format(7, base=3, fill="0")
print(tri)
print(sedem)
def razdalja(h1, h2):
    """Sprejme dve vozlišči hiperkocke in vrne razdaljo med njima"""
    #Sestavimo sezname
    d = 0
    for i in range(len(h1)):
        if h1[i] != h2[i]:
            d += 1
    return d
#print(razdalja(a, b))
def W(a, b):
    """Sprejme vozlišči a in b hiperkocke G in vrne množico Wab={x in V(G) | d(a, x) < d(b, x)}"""
    r = len(a) #dimenzija hiperkocke
    wab = set()
    for i in range(2**r): #Ko pretvorimo ta števila v binarne nize dobimo ravno vsa vozlišča v dani hiperkocki
        voz = "{0:{fill}{base}b}".format(i, base=r, fill="0")
        if razdalja(voz, a) < razdalja(voz, b):
            wab.add(voz)
    return wab

#print(W(a, b))

def jepopolnoprirejanje(S):
    """Sprejme množico povezav S v hiperkocki in vrne True, če ta množica predstavlja popolno prirejanje v hiperkocki ter False sicer"""
    #Povezava v1v2 v hiperkocki bo dvojica vozlišč (v1, v2)
    status = True
    sez = list(S)
    r = len(sez[0][0]) #dimenzija hiperkocke
    if len(sez) != 2**(r-1): #V popolnem prirejanju je med dvema vozliščema natanko ena povezava in vsaki dve povezavi nimata skupnih krajišč
        status = False
    else:
        for i in range(len(sez)):
            for j in range(i+1, len(sez)):
                if (sez[i][0] == sez[j][0]) or (sez[i][0] == sez[j][1]) or (sez[i][1] == sez[j][0]) or (sez[i][1] == sez[j][1]):
                    status = False
    return status
S = {(nula, ena), (dve, tri), (sest, sedem), (stiri, pet)}
#print (jepopolnoprirejanje({(tri, sedem)}))
print (jepopolnoprirejanje(S))

def stevilonajkrajsihpoti(a, b):
    """Vrne stevilo najkrajsih poti med vozliscema a in b v hiperkocki"""
    #Najkrajsa pot med a in b je vsaka pot dolzine razdalja(a, b)
    r = len(a) #Dimenzija hiperkocke
    d = razdalja(a, b)
    s = d
    # Takih poti med a in b dolzine s je ravno s!
    for i in range(1, d):
        s *=(d-i)
    return s

#print(stevilonajkrajsihpoti(tri, sedem))
#print(stevilonajkrajsihpoti(nula, sedem))

def najpoti(a, b, sez=[],tp=[]):
    r = len(a)
    d = razdalja(a, b)
    if a == b:
        sez.append(tp.copy())
        return sez
    if tp == []:
        tp.append(a)
    for i in range(r):
        if a[i] != b[i]:
            temp = a[:i]+b[i] + a[i+1:]
            tp.append(temp)
            sez = najpoti(temp, b, sez, tp)
            tp.pop()
    return sez

print(najpoti(nula, ena, []))
print(najpoti(nula, pet, []))
print(najpoti(nula, sedem, []))



#def najkrajsepoti(a, b):
#    """Izpiše vse najkrajše poti med a in b na hiperkocki"""
#    #Pot bomo shranili v d-sezname vozlišč, kjer je d razdalja med a in b
#    d = razdalja(a, b)
#    Sez = [[a] + [0]*(d-1) + [b] for i in range(stevilonajkrajsihpoti(a, b))]
#    print(Sez)
#    for i in range(len(Sez)):
#        pass


#najkrajsepoti(nula, sedem)


def QrvMat(r):
    """Hiperkocko dimenzije r zapiše v matriko sosednosti"""
    with open("Matrika.txt", 'w') as mat:
        A = [[0 for i in range(2**r)] for j in range(2**r)] #Matrika samih ničel
        for i in range(2**r):
            ii = "{0:{fill}{base}b}".format(i, base=r, fill="0")
             #i-ta vrstica matrike
            for j in range(i+1, 2**r):
                jj = "{0:{fill}{base}b}".format(j, base=r, fill="0")
                if razdalja(ii, jj) == 1:
                    A[i][j] = 1
                    A[j][i] = 1
        #S tem smo sestavili A
        print(A)
        for vrsta in A:
            str1 = ""
            for v in vrsta:
                str1 += str(v)  + " "

            mat.write(str1.strip(" ") + "\n")

QrvMat(3)