def Pascaltrik(n):
    """Prejme n<= 1000 in nariše Pascalov trikotnik velikosti n"""
    vrste = []
    prejsnja = []
    if n == 1:
        vrste.append("1")
    elif n == 2:
        vrste.append("  1  ")
        vrste.append("1 2 1")
    else:
        #najprej zapišemo prvi dve vrsti
        prva = (n-1)*" " + "1"
        print(prva)

        druga = (n-2)*" " + "1 1"
        print(druga)
        #Shranim številke druge vrste kot seznam trenutnih števil
        trenutna = [1, 1]
        for i in range(3, n+1):
            prejsnja = trenutna
            trenutna = [1]
            #izračunam števila trenutne vrste iz števil prejšnje
            for k in range(1, i-1):
                trenutna.append(prejsnja[k-1] + prejsnja[k])
            trenutna.append(1)
            #Iz seznama števil trenutne vrste sestavim niz
            niztrenut =""
            for num in trenutna:
                niztrenut = niztrenut + str(num)+ " "
            niztrenut = (n-i)*" " + niztrenut
            print(niztrenut)

        #      1
        #     1 1
        #    1 2 1
        #   1 3 3 1
        #  1 4 6 4 1
        #  1 5 10 5 1
        # ...
        # n števil, n-1 presledkov

Pascaltrik(3)
3*"a"
