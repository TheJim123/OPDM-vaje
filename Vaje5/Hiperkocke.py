import sys
sys.path.insert(0, 'C:/Users/Uporabnik/Documents/GitHub/OPDM-vaje/Vaje3')
import BFSAlgoritem as bfs
#Vozlišče Hiperkocke dimenzije r predstavimo z nizom 0 in 1 dolžine r
#Pretvori število (prvi argument) v binarni niz dolžine base
#str = "{0:{fill}{base}b}".format(3, base=5, fill="0")
#print(str)

Q3 = [[1, 2, 4], [0, 3, 5], [0, 3, 6], [1, 2, 7], [0, 5, 6], [1, 4, 7], [2, 4, 7], [3, 5, 6]]

nula = "{0:{fill}{base}b}".format(0, base=3, fill="0")
ena = "{0:{fill}{base}b}".format(1, base=3, fill="0")
dve = "{0:{fill}{base}b}".format(2, base=3, fill="0")
tri = "{0:{fill}{base}b}".format(3, base=3, fill="0")
stiri = "{0:{fill}{base}b}".format(4, base=3, fill="0")
pet = "{0:{fill}{base}b}".format(5, base=3, fill="0")
sest = "{0:{fill}{base}b}".format(6, base=3, fill="0")
sedem= "{0:{fill}{base}b}".format(7, base=3, fill="0")

#print(tri)
#print(sedem)
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

#print(W(tri, sedem))

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
S1 = {(nula, ena), (dve, tri), (sest, sedem), (stiri, pet)}
#print (jepopolnoprirejanje({(tri, sedem)}))
#print (jepopolnoprirejanje(S1))

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
    """Izpiše vse najkrajše poti med a in b na hiperkocki"""
    r = len(a)
    if a == b: #Če smo na koncu neke najkrajše poti (v b), jo dodamo seznamu
        sez.append(tp.copy())
        return sez
    if tp == []: #Če poti še nismo začeli, ji dodamo začetek (a)
        tp.append(a)
    for i in range(r):
        if a[i] != b[i]: #Pogledamo v katerem bitu se začetek in konec razlikujeta
            temp = a[:i]+b[i] + a[i+1:] #Sestavimo vozlišče, ki se na tem bitu ujema z b, sicer pa z a
            # Vozlišče temp je za 1 bližje koncu, kot pa trenutni a
            tp.append(temp) #temp dodamo poti in poženemo funkcijo za iskanje poti med temp in b
            sez = najpoti(temp, b, sez, tp)
            #temp odstranimo s poti, zato da lahko brez motenj obravnavamo še situacije za ostale i
            tp.pop()
    return sez

#print(najpoti(nula, ena, []))
#print(najpoti(nula, pet, []))
#print(najpoti(nula, sedem, []))


def QrvMat(r, filename):
    """Hiperkocko dimenzije r zapiše v matriko sosednosti in jo shrani v datoteko filename"""
    with open(filename, 'w') as mat:
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

#QrvMat(3, "Matrika.txt")

#Sestavimo še funkcije razdalja, W in jepopolnoprirejanje ter sestavimo novo funkcijo F, ki za vsako povezavo ab vrne Fab
def Grazdalja(graf, a, b):
    """Sprejme graf, podan z enostavnimi seznami sosedov, in par vozlišč a ter b. Vrne razdaljo med a in b na G."""
    l = bfs.BFS(a+1, graf)
    if l[b] != -1:
        return l[b]
    else:
        return "Med {} in {} v danem grafu razdalja ni definirana!".format(a, b)

#print(bfs.BFS(1, bfs.grf1))
#print(Grazdalja(bfs.grf1, 0, 9))
#print(Grazdalja(bfs.grf1, 0, 2))
def GW(graf, a, b):
    """GW sprejme graf in par vozlišč a, b ter vrne množico Wab, ki pripada danima vozliščema v danem grafu."""
    wab = set()
    for i in range(len(graf)): #Ko pretvorimo ta števila v binarne nize dobimo ravno vsa vozlišča v dani hiperkocki
        if type(Grazdalja(graf, a, i)) == type(Grazdalja(graf, b, i)):
            if type(Grazdalja(graf, a, i)) == int and (Grazdalja(graf, a, i) < Grazdalja(graf, b, i)):
                wab.add(i)
    return wab
#print(GW(bfs.grf1, 0, 9))
#print(GW(bfs.grf1, 0, 2))
#print(GW(Q3, 3, 7))

def GJepopolnoprirejanje(graf, S):
    """Sprejme graf in množico povezav na njem, predstavljeno z urejenimi pari. Vrne True, če je S popolno prirejanje v grafu in False sicer."""
    status = True
    sez = list(S)
    r = len(sez)
    if len(graf) % 2 == 1 or r != len(graf)/2: #V tem primeru graf bodisi nima dovolj vozlišč ali pa S nima pravo število povezav
        status = False
    else:
        for i in range(r): 
            if sez[i][1] not in graf[sez[i][0]]: #Preverimo, če so vse povezave v S dejansko povezave našega grafa. Če niso, S očitno ni popolno prirejanje.
                status = False
            else:
                for j in range(i+1, r): #Preverimo, če ima kak par povezav skupno krajišče
                    if (sez[i][0] == sez[j][0]) or (sez[i][0] == sez[j][1]) or (sez[i][1] == sez[j][0]) or (sez[i][1] == sez[j][1]):
                        status = False
    return status

S2 = {(0, 1), (2, 3), (6, 7), (4, 5)}

#print(jepopolnoprirejanje(S1))
#print(GJepopolnoprirejanje(Q3, S2))
#print(GJepopolnoprirejanje(Q3, {(0, 1), (2, 3)}))
#print(GJepopolnoprirejanje(bfs.grf1, {(0, 1), (2, 4), (5, 9),(3, 6), (7, 8)}))

def GFab(graf, a, b):
    """Vrne množico povezav Fab, ki imajo eno krajišče v Wab, drugo pa v Wba."""
    W1 = GW(graf, a, b)
    W2 = GW(graf, b, a)
    F = set()
    for w1 in W1:
        for w2 in W2:
            if w1 in graf[w2]: # Če sta w1 in w2 povezana, je (w1, w2) povezava v Fab
                F.add((w1, w2))
    return F

#print(GFab(Q3, 3, 7))
#print(GJepopolnoprirejanje(Q3, GFab(Q3, 3, 7)))
    
