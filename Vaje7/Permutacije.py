def factorial(k):
    f = 1
    if k == 0:
        return f
    elif k > 0:
        for i in range(1, k+1):
            f *= i
        return f

class Permutacija:
    def __init__(self, n=1):
        self.n = n
        self.p = [0 for i in range(1, n+1)] #V osnovi damo samo 0

    def izpisi(self):
        p = self.p
        print("({})".format(str(p).strip("[]")))

def prvaLEX(perm):
    """Dano začetno permutacijo spremeni v prvo permutacijo v leksikografski urejenosti."""
    n = perm.n
    perm.p = [i for i in range(1, n+1)]
    return perm

def NaslednikLEX(perm):
    """Sprejme permutacijo perm in vrne njenega naslednika v lex ureditvi."""
    p = perm.p
    n = perm.n
    
    nas = Permutacija(n)
    nas.p = p.copy()
    
    i = n-2
    while i> -1 and p[i] > p[i+1]:
        i -= 1
    if i == -1:
        return "Nedefinirano"
    
    j = n-1
    while p[j] < p[i]:
        j -=1
    s = p[i] #Zamenjamo vrednosti - transpozicija
    t = p[j] 
    nas.p[i] = t
    nas.p[j] = s

    rho = Permutacija(n)
    r = rho.p
    for k in range(i+1, n):
        r[k] = nas.p[n-k+i]

    for k in range(i+1, n):
        nas.p[k] = r[k]

    return nas

def RangLEX(perm):
    """Sprejme permutacijo in vrnje njen rang v leksikografski ureditvi."""
    n = perm.n
    p = perm.p
    rh = p.copy()

    rho = Permutacija(n)
    rho.p = rh

    r = 0
    for i in range(n):
        r = r + (rh[i]-1)*factorial(n-1-i)
        for j in range(i+1, n):
            if rh[j] > rh[i]:
                rh[j] = rh[j] -1
    return r

def DerangLEX(r, n):
    """Sprejme rang r in naravno število n ter vrne permutacijo dolžine n, ki ima rang r v lex ureditvi."""
    perm = Permutacija(n)
    p = perm.p
    p[n-1] = 1

    for j in range(1, n):
        d = (r % factorial(j+1)) // factorial(j)
        r -= factorial(j)*d
        p[n-j-1] = d+1
        for i in range(n-j, n):
            if p[i] >= d+1:
                p[i] = p[i] + 1
    return perm
            
def PermutacijeLEX(n):
    """Vrne seznam vseh permutacij dolžine n v lex ureditvi."""
    permutacije = [] #Seznam permutacij
    pi = prvaLEX(Permutacija(n))
    while pi != "Nedefinirano":
        permutacije.append(pi)
        pi = NaslednikLEX(pi)
    return permutacije


def CantorRang(perm):
    """Sprejme permutacijo perm in vrne njen rang v Cantorjevi ureditvi"""
    n = perm.n
    p = perm.p
    r = 0
    for i in range(n):
        a = 0 
        if p[i] > 1: # p[i] = k >= 2
            for j in range(i, n): #prešteje koliko števil desno od p[i] je manjših od p[i]
                if p[j] < p[i]:
                    a +=1
        r += a*factorial(p[i]-1)
    return r

def CantorDerang(r, n):
    """Sprejme vrne permutacijo dolžine n z rangom r v Cantorjevi ureditvi."""
    # Najprej določimo Cantorjeva števila za r
    # Nato števila od 1 do n damo skupaj v seznam, če imajo enako Cantorjevo število
    # Vsak ta seznam uredimo naraščajoče
    # Nato na skrajno levo mesto damo seznam prirejen največjemu Cantorjevemu številu
    # Sledi seznam za drugo največje Cantorjevo število in postopek ponavljamo, dokler ne pridemo do ničle    <- ta pristop ni pravi, ne da vredu rezultatov pri n = 4
    # Sedaj pripnemo 1
    # če imamo kak seznam, ki je prirejen Cantorjevemu številu 0, ga pripnemo na konec
    # Alternativno, 1 avtomatsko damo v seznam, ki je prirejen ničli
    if 0 <= r <= factorial(n)-1:
        a = [0 for i in range(n)] # Nastavimo a[i] = 0 s ciljem a[i] = a_i za i>=1
        #Pri tem za a[0] razglasimo t. i. a(0) = 0, število števil manjših od 1, ki so v permutaciji za 1 (nasploh v nobeni permutaciji ne more biti števila, ki je manjše od 1)
        for i in range(n-1, 0, -1): #n-1, ..., 1
            a[i] = r // factorial(i)
            r -= a[i]*factorial(i)
    #Sedaj imamo določena Cantorjeva števila za r: a[i] za i>= 1
    #Grupirajmo indekse po vrednostih Cantorjevih števil
        print(a)
        C = [[2]] #Vnos za a_1 : (po definiciji a_1 pripada številu 2)
        o = [False] + [True] +[False for i in range(n-2)] #Definira seznam, s katerim bomo sledili, če je nek indeks že bil dan v C ali ne (indeks i predstavlja število i+1 v permutaciji)
        for i in range(2, n):
            for k in range(len(C)):
                l = C[k][0]
                if a[i] == a[l-1]: #Tedaj dodamo i v C[k]
                    C[k].append(i+1)
                    o[i] = True
            if o[i] == False: #V C še ni seznama za Cantorjevo število, ki bi pripadalo i, zato ga naredimo
                k = 0
                while k < len(C) and a[C[k][0]-1] > a[i]:
                    k +=1
                if k == len(C):
                    C.append([i+1])
                    o[i] = True
                else: #a[C[k][0]-1] < a[i]:
                    C = [C[j] for j in range(k)] + [[i+1]] + [C[j] for j in range(k, len(C))] #Tako poskrbimo, da so seznami v C vedno urejeni padajoče glede na vrednosti Cantorjevih števil njihovih elementov
                    o[i] = True
        for c in C:
            c.sort()
        #print(C)
        #Sedaj vstavimo 1:
        m = 0
        while m < len(C) and a[C[m][0]-1] == C[m][0]-1:
            m +=1
        if m == len(C):
            C = C + [[1]]
        else:
            C[m] = [1] + C[m]
            #C = [C[j] for j in range(m)] + [[1]] + [C[j] for j in range(m, len(C))]
            #Treba dodat na začetek izbranega seznama
        #Sestavimo permutacijo
        perm = Permutacija(n)
        perm.p = sum(C, [])
        return perm
    else:
        return "Nedefinirano"

def VsePermutacijeCantor(n):
    """Vrne urejen seznam vseh permutacij dolžine n s pomočjo Cantorjevih števil."""
    perm = prvaLEX(Permutacija(n)) #Prva leksikografska je identiteta, kar je tudi prva v Cantorjevi urejenosti
    permutacije = [perm]
    r = CantorRang(perm) # = 0
    while r < factorial(n)-1:
        r +=1
        if CantorDerang(r, n) != "Nedefinirano":
            perm = CantorDerang(r, n)
            permutacije.append(perm)
    return permutacije

pi = Permutacija(3)
prvaLEX(pi)
