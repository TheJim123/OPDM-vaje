import kPodmnozice as kP

#Predhodnik za Lex in Kolex (nedirektno)

def PredhodnikLex(podmn):
    """Sprejme k-podmnozico v leksikografski ureditvi in vrne njenega predhodnika"""
    k = podmn.k
    n = podmn.n
    T = podmn.T
    r = kP.RangLex(podmn)
    if r == 0:
        return "Nedefinirano"
    else:
        return kP.DerangLex(r-1, k, n)

def PredhodnikKoLex(podmn):
    """Sprejme k-podmnozico v koleksikografski ureditvi in vrne njenega predhodnika"""
    k = podmn.k
    n = podmn.n
    T = podmn.T
    r = kP.RangKoLex(podmn)
    if r == 0:
        return "Nedefinirano"
    else:
        return kP.DerangKoLex(r-1, k, n)

# Poskus direktnih algoritmov:
#LEX:

def PredhodnikLex2(podmn):
    """Sprejme k-podmnozico v leksikografski ureditvi in vrne njenega predhodnika"""
    k = podmn.k
    n = podmn.n
    T = podmn.T

    U = kP.kPodmnozica(k, n)
    U.T = T.copy()

    i = k-1
    while (i > 0) and (T[i] == T[i-1]+1): #dokler so vrednosti od desne proti levi zaporedne
        i -= 1
    if i == 0: #Če smo prišli do prve koordinate
        if T[0] == 1: #T = [1, 2, 3, 4, ...]
            return "Nedefinirano"
        else: #T = [T[0], T[0] + 1, ..., T[0] + k-1]
            U.T = [T[0]-1] + [j for j in range(n+2-k, n+1)]
            return U
    else:
        if T[k-1] == n:
            if i == k-1:
                U.T[k-1] -= 1
            else:
                U.T = [T[j] for j in range(i)] + [T[i] - 1] + [T[j] for j in range(i+1, k)]
        else:
            U.T = [T[j] for j in range(i)] + [T[i] - 1] + [j for j in range(n+1-(k-i-1), n+1)]
        return U
        
#KOLEX:
def PredhodnikKoLex2(podmn):
    """Sprejme k-podmnozico v koleksikografski ureditvi in vrne njenega predhodnika"""
    k = podmn.k
    n = podmn.n
    T = podmn.T

    U = kP.kPodmnozica(k, n)
    U.T = T.copy()

    i = k-1
    while (i >= 0) and (T[i] == k - i): #Od desne proti levi gledamo, kdaj koordinata ni minimalna
        i -= 1
    if i == -1: #Vse koordinate so minimalne -> obravnavamo prvo koleksikografsko množico
        return "Nedefinirano"
    
    else: #Pomanjšamo prvo koordinato z desne, ki ni minimalna, in od nje dalje damo največje možne koordinate
        if i == k-1:
            U.T[k-1] -= 1
        else:
            U.T = [T[j] for j in range(i)] + [T[i] - j for j in range(1, k-i+1)]
        return U
