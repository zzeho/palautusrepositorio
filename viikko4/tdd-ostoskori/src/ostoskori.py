from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = []

    def tavaroita_korissa(self):
        return len(self.ostokset)

    def hinta(self):
        return sum(ostos.hinta() for ostos in self.ostokset)

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.ostokset:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaara(1)
                return

        self.ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.ostokset:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaara(-1)

                if ostos.lukumaara() == 0:
                    self.ostokset.remove(ostos)
                return

    def tyhjenna(self):
        self.ostokset.clear()

    def ostokset(self):
        return self.ostokset
