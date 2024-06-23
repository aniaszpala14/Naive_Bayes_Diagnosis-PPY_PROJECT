import pyodbc
from Models.Disease import Disease
from Models.Symptoms import Symptoms

class DatabaseConnection:
    def __init__(self):
        self.con = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'PORT=1433;'
            'DATABASE=master;'
            'UID=sa;'
            'PWD=Slodko1111*'
        )
        self.list = []
        self.list_choroby = []
        self.map_poidch = {}
        print("Connected!")
        self.podzielListPoidCh()

    def przypadkiToList(self) -> list:
        cur = self.con.cursor()
        cur.execute("""SELECT * FROM Przypadek""")
        przypadki = cur.fetchall()
        list = []
        for przypadek in przypadki:
            list.append(Symptoms(
                przypadek.kaszel, przypadek.dusznosc, przypadek.bol_w_klatce,
                przypadek.goraczka, przypadek.swiszczacy_oddech, przypadek.utrata_wagi,
                przypadek.zmeczenie, przypadek.krwioplucie, przypadek.nocne_poty,
                przypadek.splycenie_oddechu, przypadek.sinica, przypadek.apatia,
                przypadek.flegma, przypadek.obrzek_nog, przypadek.suchosc_w_ustach,
                przypadek.zmniejszony_apetyt, przypadek.utrudnione_oddyhanie,
                przypadek.szybkie_bicie_serca, przypadek.sennosc, przypadek.zawroty_glowy,
                przypadek.idCh
            ).symptoms)
        return list

    def chorobyToList(self) -> list:
        cur = self.con.cursor()
        cur.execute("""SELECT * FROM Choroba""")
        choroby = cur.fetchall()
        list_choroby = []
        for choroba in choroby:
            list_choroby.append(Disease(choroba.idCh, choroba.nazwa))
        return list_choroby

    def podzielListPoidCh(self) -> dict:
        list_przypadkow = self.przypadkiToList()
        list_choroby = self.chorobyToList()
        map_poidch = {}
        for choroba in list_choroby:
            map_poidch[choroba.idch] = choroba.nazwa
        self.map_poidch = map_poidch
        return map_poidch
