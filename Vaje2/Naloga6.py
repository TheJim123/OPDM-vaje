def preberi(str):
    '''Prebere datoteko str in iz nje sestavi polrazsirjen seznam sosedov nekega grafa'''
    f = open(str, "r")
    st = 0
    seznam = []
    for line in f:
        a = [int(i) for i in line.strip().split(" ")]
        if seznam == []: #pripravimo prazne sezname za vsa vozlišča
            for blank in range(len(a)):
                seznam.append([])
        for i in range(len(a)):
            #Za i-to in st-to vozlišče uredimo polrazširjen seznam, če sta vozlišči povezani
            if a[i] == 1 and st < i:
                #Določimo sezname s kazalci
                el1 = [i, None]
                el2 = [st, el1]
                el1[1] = el2
                #To deluje, ker python avtomatsko dela s kazalci
                seznam[i].append(el2)
                seznam[st].append(el1)

        st +=1
    return seznam

def izpisi(seznam):
    for i in range(len(seznam)):
        print("vozlišče", i)
        for j in seznam[i]:
            print(j[0], "Sosed:", j[1][0])
        print()

seznam = preberi("primer.txt")
izpisi(seznam)

