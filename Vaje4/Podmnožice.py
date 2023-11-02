class Podmnozica:
#Množica {1, 2, 3, 4, ..., n}
    def __init__(self, n=0, ar = []):
        #Dolžina glavne množice
        self.n = n
        if n > 0:
            for i in range(n):
                ar.append(0)
        self.ar = ar

    def vstavi(self, k):
        """Sprejme k, ki je neko število med 1 in n, in ga vstavi v podmnožico"""
        if self.ar[k-1] == 0:
            self.ar = [self.ar[i] if i+1 != k else 1 for i in range(self.n)]
        else:
            print("Element je že vsebovan v podmnožici!")
        return self

    def odstrani(self, k):
        """Iz podmnožice odstrani element k, če je vsebovan"""
        if self.ar[k-1] == 1:
            self.ar = [self.ar[i] if i+1 != k else 0 for i in range(self.n)]
        else:
            print("Element ni vsebovan v tej podmnožici!")
        return self

    def vsebuje(self, k):
        """Pove, če je k vsebovan v podmnožici, ali ne."""
        vsebnost = False
        if k <= self.n:
                if self.ar[k-1] == 1:
                    vsebnost = True
        return vsebnost

    def unija(self, podmn):
        """Sprejme drugo podmnožico (torej self.n == podmn.n) in vrne njuno unijo."""
        n = self.n
        unija = Podmnozica(n)
        if 1 not in podmn.ar:
            #Delamo unijo s prazno množico
            unija = self
        else:
            for i in range(1, n+1):
                if self.vsebuje(i) == True or podmn.vsebuje(i) == True:
                    unija.vstavi(i)
        return unija
    def presek(self, podmn):
        """Sprejme drugo podmnožico (torej self.n == podmn.n) in vrne njun presek."""
        n = self.n
        sek = Podmnozica(n)
        for i in range(1, n + 1):
                if self.vsebuje(i) and podmn.vsebuje(i):
                    sek.vstavi(i)
        return sek
    def simraz(self, podmn):
        """Sprejme podmnožico iste množice (self.n == podmn.n) in vrne simetrično razliko self in podmn"""
        n = self.n
        raz = Podmnozica(n)
        for i in range(1, n+1):
            if (self.vsebuje(i) and not podmn.vsebuje(i)) or (podmn.vsebuje(i) and not self.vsebuje(i)):
                raz.vstavi(i)
        return raz
    def izpis(self):
        niz = ""
        for i in range(1, self.n + 1):
            if self.vsebuje(i):
                niz = niz + str(i)+","
        niz = "{" + niz[:-1] + "}"
        return niz
def rangLex(podmn):
    """Sprejme podmnožico množice {1, 2, ..., n} in vrne njen rang v leksikografski ureditvi"""
    r = 0
    n = podmn.n
    for i in range(1, n + 1):
        k = n - i + 1
        if podmn.vsebuje(k):
            r += 2**(n-k)
    return r
def derangLex(n, r):
    """Sprejme število r med 0 in 2**n - 1 ter vrne podmnožico, ki bi ji pripadal ta rang v leksikografski ureditvi"""
    T = Podmnozica(n)
    for i in range(1, n+1):
        k = n+1 - i
        if r % 2 == 1:
            T.vstavi(k)
        r //= 2
    return T
def naslednikLex(T):
    """Vrne naslednika množice T v leksikografski ureditvi"""
    return derangLex(T.n, rangLex(T) + 1)

def urejenePodmnLex(n):
    """Vrne vse podmnožice množice {1, 2, ..., n}, urejene leksikografsko"""
    podmnozice = []
    for r in range(2**n):
        podmnozice.append(derangLex(n, r))
    return podmnozice
#Z Grayevo kodo:

def rangGray(T):
    """Vrne rang podmnožice T v zrcaljeni Grayevi kodi."""
    r = 0
    b = 0
    n = T.n
    for i in range(n, 0, -1):
        k = n + 1 - i
        if T.vsebuje(k):
            b = 1 - b
        if b == 1:
            r += 2**(i-1)
    return r
def derangGray(n, r):
    """Vrne podmnožico T množice z n elementi, ki ima rang r v zrcaljeni Grayevi kodi"""
    T = Podmnozica(n)
    bb = 0
    for i in range(n, 0, -1):
        b = r // 2**(i-1)
        if bb != b:
            T.vstavi(n-i+1)
        bb = b
        r -= b*2**(i-1)
    return T

def naslednikGray(T):
    """Vrne naslednika podmnožice T v zrcaljeni Grayevi kodi"""
    n = T.n
    P = Podmnozica(n)
    if sum(T.ar) % 2 == 0:
        P = T.simraz(Podmnozica(n).vstavi(n))
    else:
        k = n
        while k > 0 and T.vsebuje(k) == False:
            k -= 1
        if k == 1:
            return Podmnozica(n, [])
        else:
            P = T.simraz(Podmnozica(n).vstavi(k - 1))
    return  P

A = Podmnozica(3).vstavi(2)
print(A.ar)
B = Podmnozica(3).vstavi(3)
print(B.ar)
C = Podmnozica(3).vstavi(2).vstavi(3)
print(C.ar)
P = Podmnozica(3)
Y = Podmnozica(3).vstavi(1).vstavi(2)
X = Podmnozica(3).vstavi(1).vstavi(2).vstavi(3)

#print(rangGray(P))
#print(rangGray(B))
#print(rangGray(A))
#print(derangGray(3, 0).ar)
#print(derangGray(3, 1).ar)
#print(derangGray(3, 3).ar)
print(naslednikGray(B).ar)
print(naslednikGray(P).ar)
print(X.ar)
print(naslednikGray(X).ar)