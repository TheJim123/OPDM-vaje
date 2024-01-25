import math
# Naloga 1

# a)

def ranglex(mn, k, n):
    r = 0
    for i in range(1, k+1):
        a = 1 if i == 1 else mn[i-2] + 1
        if a <= mn[i-1] -1:
            for j in range(a, mn[i-1]):
                r += math.comb(n-j, k-i)
    return  r

def rangizpitna(pi):
    n = len(pi)
    fiksne = []
    nefiksne = []
    for i in range(n):
        if pi[i] == i+1:
            fiksne.append(pi[i])
        else:
            nefiksne.append(pi[i])
    r = 2*ranglex(fiksne, n-3, n)
    if nefiksne[0] > nefiksne[1]:
        r += 1
    return r

#test

#pi = [5,2, 1, 4, 3]
#print(rangizpitna(pi)) (= 11)
# b)

def deranglex(r, k, n):
    x = 1
    mn = [0]*k
    for i in range(1, k+1):
        while math.comb(n-x, k-i) <= r:
            r -= math.comb(n-x, k-i)
            x +=1
        mn[i-1] = x
        x +=1
    return mn

def derangizpitna(r, n):
    pi = [0]*n
    fiksne = deranglex(r // 2, n-3, n)
    for i in fiksne:
        pi[i-1] = i
    nefiksne = []
    for i in range(n):
        if pi[i] == 0:
            nefiksne.append(i+1)
    if r%2 == 0:
        pi[nefiksne[0]-1] = nefiksne[1]
        pi[nefiksne[1] - 1] = nefiksne [2]
        pi[nefiksne[2] - 1] = nefiksne[0]
    else:
        pi[nefiksne[0] - 1] = nefiksne[2]
        pi[nefiksne[1] - 1] = nefiksne[0]
        pi[nefiksne[2] - 1] = nefiksne[1]
    return  pi

#test
for i in range(20):
    print(derangizpitna(i, 5), i)


# Naloga 2

def preberi(str):
    f = open(str, 'r')
    mat = []
    for line in f:
        a = [int(i) for i in line.strip().split(" ")]
        mat.append(a)
    return mat

def vrniSosede(mat, par):
    i = par[0]
    j = par[1]
    sosedi = []
    x = [i-1, i-1,i-1, i, i, i+1, i+1, i+1]
    y = [j-1, j, j+1, j-1, j+1, j-1, j, j+1]
    for k in range(len(x)):
        if x[k] >= 0 and x[k] < len(mat) and y[k] >= 0 and y[k] < len(mat) and mat[x[k]][y[k]] == 1:
            sosedi.append((x[k], y[k]))
    return sosedi

def povezaniDeli(mat):
    velikosti = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 1:
                mat[i][j] = 2
                vel = 1
                # bfs
                vrsta = [(i, j)]
                while len(vrsta) > 0:
                    u = vrsta.pop()
                    sosedi = vrniSosede(mat, u)
                    for s in sosedi:
                        mat[s[0]][s[1]] = 2
                        vel += 1
                        vrsta.append(s)
                velikosti.append(vel)
    return velikosti, len(velikosti)

#matrika = preberi("matrika.txt")
#print(povezaniDeli(matrika))