def Preberivsez(dat):
    '''Funkcija sprejme datoteko dat v katero je zapisana matrika sosedov grafa G in s pomočjo te zapiše predstavitev grafa G s seznami sosedov.'''
    file = open(dat, "r")
    S = [0]
    P = []
    st = 0
    for line in file:
        #seznam števil v vrsti
        a = [int(i) for i in line.strip().split(" ")]
        n = len(a)
        sos = [i for i in range(n) if a[i] == 1]
        P.append(sos)
        st +=1
        add = S[-1] + len(sos)
        #print(add)
        S.append(add)
    S.remove(S[-1])
    return S, P


#print(Preberivsez("primer.txt"))

