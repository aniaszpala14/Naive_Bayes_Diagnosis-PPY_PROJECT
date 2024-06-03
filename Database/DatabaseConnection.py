import sqlite3

from Models.Symptoms import Symptoms


class Connection():
    con: sqlite3.Connection

    def __init__(self):
        self.con = sqlite3.connect('master')

    def przypadkiToList(self) -> []:
        self.con.row_factory = sqlite3.Row
        cur = self.con.cursor()
        cur.execute("""SELECT * FROM Przypadek""")
        przypadki = self.cur.fetchall()
        list = []
        for przypadek in przypadki:
            cur.execute("""SELECT * FROM Choroba WHERE idCh = przypadek[idCh]""")
            choroba = cur.fetchall()
            list.append(Symptoms(przypadek['apatia'], przypadek['bol_w_klatce'], przypadek['goraczka'],
                                 przypadek['kaszel'], przypadek['flegma'], przypadek['krwioplucie'],
                                 przypadek['nocne_poty'], przypadek['obrzek_nog'], przypadek['sennosc'],
                                 przypadek['sinica'], przypadek['splycenie_oddechu'], przypadek['suchosc_w_ustach'],
                                 przypadek['swiszczacy_oddech'], przypadek['szybkie_bicie_serca'],
                                 przypadek['utrudnione_oddychanie'], przypadek['zawroty_glowy'], przypadek['zmeczenie'],
                                 przypadek['zmniejszony'], choroba[]))
