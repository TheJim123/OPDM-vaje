import razsirjeniSeznam as rs
def obstajaPovezava(graf, a, b):
    """Funkcija prejme graf predstavljen z razširjenimi seznami in dve vozlišči ter pove, če sta vozlišči v grafu povezani"""
    if a< 0 or b < 0 or a>= len(graf) or b >= len(graf):
        return False
    if graf[a] == [] or graf[b] == []:
            return False
    el = graf[a]
    while el != None:
        if el.vj == b:
            return True
        el = el.n
    return False

def sosedi(graf, a):
    """Funkcija prejme graf podan z razširjenimi seznami sosedov in vozlišče ter izpiše vse njegove sosede v grafu."""
    sosed = []
    el = graf[a]
    while el != None:
        if el.vi == a:
            sosed.append(el.vj)
        el = el.n
    return sosed

def dodajPovezavo(graf, a, b):
    if b in sosedi(graf, a):
        print("Vozlišči sta že povezani!")
    else:
        el1 = rs.Element(a, b)
        el2 = rs.Element(b, a)
        el1.s = el2
        el2.s = el1
        if graf[a] == []:
            graf[a] = el1
        else:
            graf[a].p = el1
            el1.n = graf[a]
            graf[a] = el1
        if graf[b] == []:
            graf[b] = el2
        else:
            graf[b].p = el2
            el2.n = graf[b]
            graf[b] = el2

def odstraniPovezavo(graf, a, b):
    """Funkcija sprejme graf in par vozlišč in iz grafa odstrani povezavo med danima vozliščema, če obstaja"""
    el1 = graf[a]
    #Iz seznamov odstranimo tistega, ki predstavlja povezavo med a in b
    while el1 != None:
        if el1.vj == b:
            # Uredimo kazalce za povezavo za a
            el1.n.p = el1.p
            el1.p.n = el1.n
            #uredimo kazalce za povezavo za b
            el2 = el1.s
            el2.p.n = el2.n
            el2.n.p = el2.p
            #odstranimo polja
            #graf.remove(el1)
            #graf.remove(el2)
            return graf

        el1 = el1.n
    print("Vozlišči nista povezani!")

def OdstraniPovezave(graf, a):
    el = graf[a]
    while el != None:
        odstraniPovezavo(graf, el.vi, el.vj)
        el = el.n
def IzpisiPovezave(graf):
    povezave = []
    for i in range(len(graf)):
        el = graf[i]
        while el != None and el != []:
            if el.vi > el.vj:
                povezave.append([el.vi, el.vj])
            el = el.n
    return povezave



#graf = rs.preberi("primer.txt")
#rs.izpisiGraf(graf)
#print(obstajaPovezava(graf, 3, 1))
#print(obstajaPovezava(graf, 1, 2))
#print(sosedi(graf, 1))
#print(sosedi(graf, 6))
#dodajPovezavo(graf, 1, 2)
#print(obstajaPovezava(graf, 1, 2))
#odstraniPovezavo(graf, 1, 3)
#print(obstajaPovezava(graf, 1, 3))
#rs.izpisiGraf(graf)
#print(IzpisiPovezave(graf))
