def RazMatrik(A, B):
    """Funkcija prejme dve matriki enakih dimenzij in vrne njuno razliko"""
    n = len(A)
    m = len(A[0])
    C = []
    i = 0
    while i <= n-1:
        j = 0
        rowC = []
        while j <= m-1:
            rowC.append(A[i][j] - B[i][j])
            j += 1
        C.append(rowC)
        i += 1
    return C


# Test
A= [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(A[0])
print(RazMatrik(A, A))
print(RazMatrik(A, B))
print(RazMatrik(B, A))