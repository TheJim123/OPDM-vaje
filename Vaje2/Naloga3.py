import matrika
import Naloga2

def Minstopnja(mat):
    min = len(mat)
    for i in range(len(mat)):
        m = len(Naloga2.Sosede(mat, i))
        if m < min:
            min = m
    return min

def Maxstopnja(mat):
    max = 0
    for i in range(len(mat)):
        M = len(Naloga2.Sosede(mat, i))
        if M > max:
            max = M
    return max

def Zminstopnjo(mat):
    m = Minstopnja(mat)
    zmin = []
    for i in range(len(mat)):
        if len(Naloga2.Sosede(mat, i)) == m:
            zmin.append(i)
    return zmin
            
def Zmaxstopnjo(mat):
    M = Maxstopnja(mat)
    zmax = []
    for i in range(len(mat)):
        if len(Naloga2.Sosede(mat, i)) == M:
            zmax.append(i)
    return zmax
            
