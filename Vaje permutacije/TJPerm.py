import math
def TJrang(pi):
    """Sprejme permutacijo pi in vrne njen rang v Trotter-Johnsonovi ureditivi."""
    r = 0
    n = len(pi)
    for j in range(2, n+1):
        k = 1
        i = 1
        while pi[i-1] != j:
            if pi[i-1] < j:
                k += 1
            i += 1
        if r % 2 == 0:
            r = j*r + j - k
        else:
            r = j*r + k - 1
    return r

def TJderang(r, n):
    """Sprejme število r med 0 in n!-1 in vrne permutacijo pi dolžine n, ki ima v Trotter-Johnsonovi ureditvi rang r"""
    pi = [1]*n
    r2 = 0
    for j in range(2, n+1):
        r1 = math.floor(r * math.factorial(j) / math.factorial(n))
        k = r1 - j*r2
        if r2 % 2 == 0:
            for i in range(j-1, j-k-1, -1):
                pi[i] = pi[i-1]
            pi[j-k-1] = j
        else:
            for i in range(j-1, k, -1):
                pi[i] = pi[i-1]
            pi[k] = j
        r2 = r1
    return pi

#Test, da dela:
# n = 5
#for i in range(120):
#    pi = TJderang(i, n)
#    print(pi, TJrang(pi))

def parnost(pi, n):
    """Sprejme permutacijo pi in vrne 0, če je soda ter 1, če je pi liha. Pri tem gleda le do n-tega mesta"""
    a = [0]*n
    c = 0
    for i in range(1, n+1):
        if a[i-1] == 0:
            c += 1
            a[i-1] = 1
            j = i
            while pi[j-1] != i:
                j = pi[j-1]
                a[j-1] = 1
    return (n-c)%2

#print(parnost([1, 2, 4, 3]))

def TJnaslednik(pi):
    """Sprejme permutacijo pi in vrne njenega naslednika v Trotter-Johnsonovi ureditvi."""
    n = len(pi)
    st = 0
    ro = pi.copy()
    konec = False
    m = n
    while m > 1 and not konec:
        k = ro.index(m) + 1
        for i in range(k, m):
            ro[i-1] = ro[i]
        p = parnost(ro, m-1)
        if p == 0:
            if k != 1:
                pi[k+st-1], pi[k+st-2] = pi[k+st-2], pi[k+st-1]
                konec = True
            else:
                st +=1
                m -=1
        else:
            if k != m:
                pi[k+st-1], pi[k+st] = pi[k+st], pi[k+st-1]
                konec = True
            else:
                m -=1
    if m == 1:
        print("Nedefinirano")
        for i in range(n):
            pi[i] = i+1
    return pi

pi =[1, 2, 3, 4, 5]
for i in range(120):
    print(pi, TJrang(pi))
    pi = TJnaslednik(pi)
