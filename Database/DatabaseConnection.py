import pyodbc
from pyodbc import Row
from Models.Disease import Disease
from Models.Symptoms import Symptoms


class DatabaseConnection:
    def __init__(self):
        self.con = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'PORT=1433;'
            'DATABASE=ppy;'
            'UID=sa;'
            'PWD=ania1410@DOCKER'
        )
        self.list = []
        self.list_diseases = []
        self.map_by_idch = {}
        print("Connected!")
        self.divide_list_by_idCh()

    def cases_to_list(self) -> list:
        cur = self.con.cursor()
        cur.execute("""SELECT * FROM Przypadek""")
        cases = cur.fetchall()
        list = []
        for case in cases:
            list.append(Symptoms(
                case.kaszel, case.dusznosc, case.bol_w_klatce,
                case.goraczka, case.swiszczacy_oddech, case.utrata_wagi,
                case.zmeczenie, case.krwioplucie, case.nocne_poty,
                case.splycenie_oddechu, case.sinica, case.apatia,
                case.flegma, case.obrzek_nog, case.suchosc_w_ustach,
                case.zmniejszony_apetyt, case.utrudnione_oddychanie,
                case.szybkie_bicie_serca, case.sennosc, case.zawroty_glowy,
                case.idCh
            ).symptoms)
        return list

    def diseases_to_list(self) -> list:
        cur = self.con.cursor()
        cur.execute("""SELECT * FROM Choroba""")
        diseases = cur.fetchall()
        list_diseases = []
        for disease in diseases:
            list_diseases.append(Disease(disease.idCh, disease.nazwa))
        return list_diseases

    def divide_list_by_idCh(self) -> dict:
        list_diseases = self.diseases_to_list()
        map_by_idch = {}
        for disease in list_diseases:
            map_by_idch[disease.idch] = disease.nazwa
        self.map_by_idch = map_by_idch
        return map_by_idch

    def is_model_in_database(self) -> Row | None:
        cur = self.con.cursor()
        cur.execute("SELECT 1 FROM model WHERE nazwa = 'GaussianNB'")
        return cur.fetchone()

    def add_model(self, model: bytes):
        cur = self.con.cursor()
        cur.execute("INSERT INTO model (nazwa, model) VALUES (?, ?)", ('GaussianNB', model))

    def get_model(self) -> bytes:
        cur = self.con.cursor()
        cur.execute("SELECT e.model FROM model e WHERE e.nazwa = 'GaussianNB'")
        row = cur.fetchone()
        return row[0]

    def close_connection(self):
        self.con.close()

    def commit(self):
        self.con.commit()
