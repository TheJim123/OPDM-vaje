def vsebuje(sez, a, m=0, n=None):
    """Funkcija sprejme urejen seznam celih števil sez in celo število a ter parametra m in n, ki določata indekse v katerih iščemo a. Vrne True, če je a vsebovan v sez in False sicer."""
    vseb = False
    if n == None:
        n = len(sez)
    # Če je a manjši od najmanjšega elementa a ali večji od največjega,
    # potem očitno ni v seznamu
    if sez[m] <= a and a <= sez[n - 1]:
        # Če je del seznama, ki ga gledamo, daljši od 1, ugotovimo, v kateri polovici bi a lahko bil
        l = (n - m) // 2
        if (n-m) > 1:
            # Če to velja je a v spodnji polovici dela, ki ga gledamo in lahko zgornjo ignoriramo.
            if a <= sez[m + l-1]:
                # Premaknemo zgornjo mejo, da ne obravnavamo nerelevantnih delov.
                n = m+l
                # Ponovimo postopek za ta del seznama
                return vsebuje(sez, a, m, n)
            # če zgornji pogoj ne velja, je a v drugi polovici
            else:
                m += l
                # Ponovimo postopek za ta del seznama sez
                return vsebuje(sez, a, m, n)
        # če je del sez, ki ga gledamo, dolg 1 je vsebovanost enostavno preveriti
        elif (n-m) == 1 and sez[m] == a:
            vseb = True
    return vseb

print(vsebuje([1, 2, 3, 4, 5], 0))
print(vsebuje([1, 2, 3, 4, 5], 1))
print(vsebuje([1, 2, 3, 4, 5], 2))
print(vsebuje([1, 2, 3, 4, 5], 3))
print(vsebuje([1, 2, 3, 4, 5], 4))
print(vsebuje([1, 2, 3, 4, 5], 5))
print(vsebuje([1, 2, 3, 4, 5], 6))
print(vsebuje([1, 2, 3, 4, 5], 7))


