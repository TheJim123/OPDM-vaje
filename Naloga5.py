def Pascaltrik(n):
    """Prejme n<= 1000 in nariše Pascalov trikotnik velikosti n"""
    vrste = []
    if n == 1:
        vrste.append("1")
    elif n == 2:
        vrste.append("     \n")
        vrste.append("1 2 1")
    #else:
        #prva = (n-1)*" " + "1" + (n-1*" "
        #druga = (n-2)*" " + "1 1" + (n-2)*" "
        #i = 1
        #while i <= n:


    #for vrsta in vrste:
        #print(vrsta)
    return vrste


        # 1
        # 1 1
        # 1 2 1
        # 1 3 3 1
        # 1 4 6 4 1
        # 1 5 10 5 1
        # ...
        # n števil, n-1 presledkov

    Pascaltrik(1)