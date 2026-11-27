import unittest
from ostoskori import Ostoskori
from ostos import Ostos
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        sokeri = Tuote("Sokeri", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(sokeri)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        sokeri = Tuote("Sokeri", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(sokeri)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_hinta(self):
        maito = Tuote("maito", 5)
        leipa = Tuote("leipä", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)
        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_saman_tuotteen_maara(self):
        maito = Tuote("maito", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_hinta(self):
        maito = Tuote("maito", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 10)

    def test_yhden_tuotteen_jalkeen_ostokset_palauttaa_yhden_ostos_olion(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertIsInstance(ostokset[0], Ostos)

    def test_yhden_tuotteen_jalkeen_ostos_oliolla_oikea_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_jalkeen_ostokset_palauttaa_kaksi_ostos_oliota(self):
        maito = Tuote("Maito", 3)
        sokeri = Tuote("Sokeri", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(sokeri)
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_jalkeen_ostokset_palauttaa_yhden_ostos_olion(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_tuotteen_ostos_oliolla_oikea_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 2)

    def test_saman_tuotteen_poistaminen_vahentaa_maaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].lukumaara(), 1)

    def test_yhden_tuotteen_poistamisen_jalkeen_kori_on_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)

    def test_tyhjenna_poistaa_kaikki_ostokset(self):
        maito = Tuote("Maito", 3)
        sokeri = Tuote("Sokeri", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(sokeri)
        self.kori.tyhjenna()
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)