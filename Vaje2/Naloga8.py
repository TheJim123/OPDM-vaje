import Naloga7 as n7
def UrediRazsirjenSezSosedov(sez):
    """Sprejme razširjen seznam sosedov in ga uredi, ter vrne"""
    #Pripravimo prazne sezname sosedov
    Urejen = []
    for _ in sez:
        Urejen.append([])
    n = len(sez)
    for i in range(n):
        while sez[n-i] != []:
            for j in range(len(sez[n-i])):
                del sez[n-i][j]
                n7.dodajPovezavo(Urejen, j, i)
    return Urejen

#Še nisem testiral
