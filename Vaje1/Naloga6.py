def vsebuje(sez, a):
    """Funkcija sprejme urejen seznam celih števil sez in celo število a. Vrne True, če je a vsebovan v sez in False sicer."""
    vseb = False
    l = len(sez)
    #Če je a manjši od najmanjšega elementa a ali večji od največjega,
    #potem očitno ni v seznamu
    if sez[0] <= a and a <= sez[l-1]:
        # Če je seznam daljši od 1 ugotovimo, v kateri polovici bi a lahko bil
        if l > 1:
            m =  l // 2
            #Če to velja je a v spodnji polovici in lahko zgornjo ignoriramo.
            if a <= sez[m-1]:
                #Prepišemo seznam sez v seznam, ki vsebuje samo relevantno polovico
                sez = [sez[i] for i in range(m)]
                #Ponovimo postopek za nov sez
                return vsebuje(sez, a)
            #če zgornji pogoj ne velja, je a v drugi polovici
            else:
                #Prepišemo seznam sez v seznam, ki vsebuje samo relevantno polovico
                sez = [sez[i] for i in range(m, l)]
                #Ponovimo postopek za nov sez
                return vsebuje(sez, a)
        #če je sez dolg 1 je vsebovanost enostavno preveriti
        elif l == 1 and sez[0] == a:
            vseb = True
    return vseb
                
    
    
    
