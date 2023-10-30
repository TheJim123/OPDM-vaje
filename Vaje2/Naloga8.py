import math
import Naloga7 as n7
import razsirjeniSeznam as rs

def UrediRazsirjenSezSosedov(sez):
    """Sprejme razširjen seznam sosedov in ga uredi, ter vrne"""
    n = len(sez)
    #V našem branju grafa ima "sez" dolžino, ki je enaka kvadratu števila vozlišč
    m = int(math.sqrt(n))
    Urejen = [[] for i in range(m)]
    for i in range(m):
        #Najprej pogledamo sodede zadnjega vozlišča
        el = graf[m-i-1]
        while el != None:
            if Urejen[el.vj] == [] and Urejen[el.vi] == []:
                Urejen[el.vj] = rs.Element(el.vj, el.vi, None, None, el.s.s)
                Urejen[el.vi] = rs.Element(el.vi, el.vj, None, None, el.s)
            elif Urejen[el.vj] == [] and Urejen[el.vi] != []:
                Urejen[el.vj] = rs.Element(el.vj, el.vi, None, None, el.s.s)
                el2 = rs.Element(el.vi, el.vj)
                Urejen[el.vi].p = el2
                el2.n = Urejen[el.vi]
                Urejen[el.vi] = el2
            elif Urejen[el.vj] != [] and Urejen[el.vi] == []:
                Urejen[el.vi] = rs.Element(el.vi, el.vj, None, None, el.s)
                el2 = rs.Element(el.vj, el.vi)
                Urejen[el.vj].p = el2
                el2.n = Urejen[el.vj]
                Urejen[el.vj] = el2
            else:
                n7.dodajPovezavo(Urejen, el.vj, el.vi)
            el = el.n
    return Urejen

graf = rs.preberi("primer.txt")
rs.izpisiGraf(graf)
urejen = UrediRazsirjenSezSosedov(graf)
rs.izpisiGraf(urejen)
