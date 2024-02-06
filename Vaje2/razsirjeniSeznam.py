class Element:
    def __init__(self, vi = -1, vj = -1, p = None, n = None, s=None):
        self.vi = vi
        self.vj = vj
        self.p = p
        self.n = n
        self.s = s
    def izpisi(self):
        print("[{},{},{},{},{}]".format(self.vi, self.vj,
                                        "none" if self.p == None else "[{}, {}]".format(self.p.vi, self.p.vj),
                                        "none" if self.n == None else "[{}, {}]".format(self.n.vi, self.n.vj),
                                        "none" if self.s == None else "[{}, {}]".format(self.s.vi, self.s.vj)))
def preberi(str):
    f = open(str, 'r')
    graf = []
    stevilkaVrstice = 0
    for line in f:
        a = [int(i) for i in line.strip().split(" ")]
        #V graf dodamo prazne sezname sosedov
        for _ in range(len(a)):
            graf.append([])
        #Upoštevamo v kateri vrstici smo in gledamo nad diagonalo matrike, da se ne ponavljamo
        for i in range(len(a)):
            if i < stevilkaVrstice and a[i] == 1:
                el1 = Element(stevilkaVrstice, i)
                el2 = Element(i, stevilkaVrstice)
                #Spremenimo soseda
                el1.s = el2
                el2.s = el1
                #Preverimo, če v seznamu že imamo kako polje
                if graf[stevilkaVrstice] == []:
                    graf[stevilkaVrstice] = el1
                else:
                    graf[stevilkaVrstice].p = el1
                    el1.n = graf[stevilkaVrstice]
                    graf[stevilkaVrstice] = el1
                if graf[i] == []:
                    graf[i] = el2
                else:
                    graf[i].p = el2
                    el2.n = graf[i]
                    graf[i] = el2
        stevilkaVrstice +=1
    return graf

def izpisiGraf(graf):
    for i in graf:
        el = i
        if el != []:
            while el != None:
                el.izpisi()
                el = el.n

#graf = preberi("primer.txt")
#izpisiGraf(graf)
