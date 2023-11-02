import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

def narisi(mat):
    A = np.array(mat)
    G = nx.Graph(A)
    layout = nx.spring_layout(G)
    nx.draw(G, layout, with_labels=True)
    plt.show()

# Matrika sosednosti grafa G je matrika A, za katero velja a_ij = 1,
# če med vozlišči v_i in v_j obstaja povezava in a_ij = 0 sicer.
def Preberi(dat):
    '''Odpre datoteko dat in z njeno pomočjo sestavi matriko sosednosti nekega grafa'''
# dat je v nizu predstavljeno ime datoteke
    f = open(dat, 'r')
    mat = []
    for line in f:
        a = [int(i) for i in line.strip().split(' ')]
        mat.append(a)
    return mat
mat = Preberi("primer.txt")
#for i in mat:
#    print(i)
narisi(mat)
