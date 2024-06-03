import sqlite3

from Models.Disease import  Disease
from Models.Symptoms import Symptoms
class Connection():
    con: sqlite3.Connection
    list: []
    list_choroby: []
    map_poidCh: {}

    def __init__(self):
        self.con = sqlite3.connect('master')

    def przypadkiToList(self) -> []:
        self.con.row_factory = sqlite3.Row
        cur = self.con.cursor()
        cur.execute("""SELECT * FROM Przypadek""")
        przypadki = self.cur.fetchall()
        list = []
        for przypadek in przypadki:
          # cur.execute("""SELECT * FROM Choroba WHERE idCh = przypadek[idCh]""")
          #  choroba = cur.fetchall()
            list.append(Symptoms(przypadek['kaszel'],przypadek['dusznosc'],przypadek['bol_w_klatce'],
                                 przypadek['goraczka'],przypadek['swiszczacy_oddech'],przypadek['utrata_wagi'],
                                 przypadek['zmeczenie'],przypadek['krwioplucie'],przypadek['nocne_poty'],
                                 przypadek['splycenie_oddechu'],przypadek['sinica'],przypadek['apatia'],przypadek['flegma'],
                                 przypadek['obrzek_nog'],przypadek['suchosc_w_ustach'],przypadek['zmniejszony_apetyt'],
                                 przypadek['utrudnione_oddychanie'],przypadek['szybkie_bicie_serca'],
                                 przypadek['sennosc'],przypadek['zawroty_glowy'],przypadek['idCh']))

    def chorobyToList(self):
        self.con.row_factory = sqlite3.Row
        cur = self.con.cursor()
        cur.execute("""SELECT * FROM Choroba""")
        choroby = cur.fetchall()
        list_choroby = []
        for choroba in choroby:
            list_choroby.append(Disease(choroba['idCh'],choroba['nazwa']))
        return list_choroby

    def podzielListPoidCh(self):
        list = self.przypadkiToList()
        list_choroby = self.chorobyToList()
        map_poidCh = {}
        for choroba in list_choroby:
            map_poidCh[choroba.idCh] = [x for x in list if x.choroba == choroba.idCh]
        return map_poidCh






