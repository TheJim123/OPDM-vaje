def uredipadajoce(seznam):
    if seznam != []:
        urejen = []
        while seznam != []:
            m = max(seznam)
            seznam.remove(m)
            urejen.append(m)
        return urejen
    else:
        return print("Seznam je prazen!")
