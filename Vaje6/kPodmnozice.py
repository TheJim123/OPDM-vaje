import math
class kPodmnozica:
    def __init__(self, k=0, n=0): #predpostavimo, da je 0 < k <= n
        self.k = k
        self.n = n
        self.T = self.k * [0]

    def izpisi(self):
        print("{}" if self.T == (self.k * [0]) else str(self.T))
        
    def prvaLex(self):
        for i in range(self.k):
            self.T[i] = i+1

    def prvaKoLex(self):
        for i in range(self.k):
            self.T[i] = self.k - i

#Leksikografska:
        
def UstrezaLex(podmn):
    if podmn.T[0] < 1 or podmn.T[-1] > podmn.n:
        return False
    else:
        for i in range(podmn.k - 1):
            if podmn.T[i] >= podmn.T[i+1]:
                return False
        return True
    
def RangLex(podmn):
    k = podmn.k
    n = podmn.n
    T = podmn.T
    if not UstrezaLex(podmn):
        return "Ne ustreza leksikografski ureditvi!"
    else:
        r = 0
        L = 1
        for i in range(k):
            if L <= T[i] - 1:
                for j in range(L, T[i]):
                    r += math.comb(n - j, k-i-1)
            L = T[i] + 1
        return r

def DerangLex(r, k, n):
    P = kPodmnozica(k, n)
    x = 1
    for i in range(k):
        while math.comb(n - x, k - i - 1) <= r:
            x += 1
            r -= math.comb(n - x + 1,k-i-1)
        P.T[i] = x
        x += 1
    return P

def NaslednjikLex(podmn):
    k = podmn.k
    n = podmn.n
    T = podmn.T

    U = kPodmnozica(k, n)
    U.T = T.copy()
    
    i = k-1
    if UstrezaLex(podmn):
        while (i >= 0) and (T[i] == n - k + (i + 1)):
            i -= 1
        if i == -1:
            return "Nedefinirano"
        else:
            for j in range(i, k):
                U.T[j] = T[i] + (j - i) + 1
        return U

def LexPodmn(k, n):
    """Za naravni števili 0 < k <= n vrne seznam k-podmnožic v leksikografski ureditvi."""
    P = kPodmnozica(k, n)
    P.prvaLex() #Pripravi prvo k-podmnozico
    #P.izpisi()
    Sez = [P] #Jo da v seznam
    
    L = math.comb(n, k)
    i = 1
    while i <= L-1:
        P = NaslednjikLex(P)
        #P.izpisi()
        Sez.append(P)
        i += 1
    return Sez
        
# Koleksikografska:        
        
def UstrezaKoLex(podmn):
    if podmn.T[0] > podmn.n or podmn.T[-1] < 1:
        return False
    else:
        for i in range(podmn.k - 1):
            if podmn.T[i] <= podmn.T[i+1]:
                return False
        return True
    
def RangKoLex(podmn):
    k = podmn.k
    n = podmn.n
    T = podmn.T
    if not UstrezaKoLex(podmn):
        return "Ne ustreza koleksikografski ureditvi!"
    else:
        r = 0
        for i in range(k):
            r += math.comb(T[i] - 1, k-i)
        return r

def DerangKoLex(r, k, n):
    P = kPodmnozica(k, n)
    x = n
    for i in range(k):
        while r < math.comb(x, k - i):
            x -= 1
        P.T[i] = x + 1
        r -= math.comb(x ,k-i)
    return P

def NaslednjikKoLex(podmn):
    k = podmn.k
    n = podmn.n
    T = podmn.T

    U = kPodmnozica(k, n)
    U.T = T.copy()
    
    i = k-1
    if UstrezaKoLex(podmn):
        while (i > 0) and (T[i] == T[i-1] - 1):
            i -= 1
        if i == 0 and T[0] == n:
            return "Nedefinirano"
        else:
            U.T[i] += 1
            j = 1
            for l in range(k-1, i, -1):
                U.T[l] = j
                j += 1
        return U

def KoLexPodmn(k, n):
    """Za naravni števili 0 < k <= n vrne seznam k-podmnožic v koleksikografski ureditvi."""
    P = kPodmnozica(k, n)
    P.prvaKoLex() #Pripravi prvo k-podmnozico
    #P.izpisi()
    Sez = [P] #Jo da v seznam
    
    L = math.comb(n, k)
    i = 1
    while i <= L-1:
        P = NaslednjikKoLex(P)
        #P.izpisi()
        Sez.append(P)
        i += 1
    return Sez
  
# Rang, Derang in Naslednjik za Leksikografsko preko koleksikografske:

def pretvori(podmn):
    """Sprejme k-podmnožico T in vrne množico {n - i + 1; i \in T}"""
    T = podmn.T
    k = podmn.k
    n = podmn.n
    U = kPodmnozica(k, n)
    for i in range(k):
        U.T[i] = n - T[i] + 1
    return U

def RangLex2(podmn):
    n = podmn.n
    k = podmn.k
    L = math.comb(n, k)
    U = pretvori(podmn)
    return L - 1 - RangKoLex(U)

def DerangLex2(r, k, n):
    L = math.comb(n, k)
    t = L - 1 - r # koleksikografski rang za T'
    U = DerangKoLex(t, k, n) # Naš T'. Upoštevamo, da je (T')' = T
    return pretvori(U)

def NaslednjikLex2(podmn):
    
    t = RangKoLex(pretvori(podmn))
    if t == 0:
        return "Nedefinirano"
    else:
        r = math.comb(n, k) - t #rang naslednika od podmn v lex
        return DerangLex(r)
                
