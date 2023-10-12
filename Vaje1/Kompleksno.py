import math
class Kompleksno():
    """Reprezentacija kompleksnih števil"""
    def __init__(self, re=0, im=0):
            self.re = re
            self.im = im

    def izpis(self):
        """Izpiše kompleksno število v obliki a+bi"""
        print(str(self.re) + "+" + str(self.im)+"i")

    def vsota(self, z1):
        """Sešteje dve kompleksni števili"""
        new_re = z1.re + self.re
        new_im = z1.im + self.im
        return Kompleksno(new_re, new_im)
    def produkt(self, z1):
        """Zmnoži dve kompleksni števili"""
        new_re = z1.re * self.re - z1.im * self.im
        new_im = z1.re * self.im + z1.im * self.re
        return Kompleksno(new_re, new_im)

    def konjugiraj(self):
        """Konjugira kompleksno število"""
        new_re = self.re
        new_im = -self.im
        return Kompleksno(new_re, new_im)
    def absolutna(self):
        """izračuna absolutno vrednost kompleksnega števila"""
        return math.sqrt(self.re**2 + self.im **2)
    def inv(self):
        a = self.absolutna()
        inv_re = self.re / a
        inv_im = - self.im / a
        return Kompleksno(inv_re, inv_im)



# testing stuff

t = Kompleksno()
k = Kompleksno(3, 4)
h = Kompleksno((-20), 15)
i = Kompleksno(0, 1)
t.izpis()
h.izpis()
k.vsota(h).izpis()
k.produkt(i).izpis()
h.konjugiraj().izpis()
print(i.absolutna())
print(k.absolutna())
i.inv().izpis()