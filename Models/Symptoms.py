from enum import Enum


class Symptoms:
    apatia: str
    kaszel: str
    dusznosc: str
    bol_w_klatce: str
    goraczka: str
    swiszczacy_oddech: str
    utrata_wagi: str
    zmeczenie: str
    krwioplucie: str
    nocne_poty: str
    splycenie_oddechu: str
    sinica: str
    flegma: str
    obrzek_nog: str
    suchosc_w_ustach: str
    zmniejszony_apetyt: str
    utrudnione_oddychanie: str
    szybkie_bicie_serca: str
    sennosc: str
    zawroty_glowy: str
    choroba: str
    symptoms: []

    def __init__(self, apatia: str, bol_w_klatce: str, goraczka: str, kaszel: str, flegma: str,
                 krwioplucie: str, nocne_poty: str, obrzek_nog: str, sennosc: str, sinica: str,
                 splycenie_oddechu: str, suchosc_w_ustach: str, swiszczacy_oddech: str, szybkie_bicie_serca: str,
                 utrata_wagi: str, utrudnione_oddychanie: str, zawroty_glowy: str, zmeczenie: str,
                 zmniejszony_apetyt: str, dusznosc: str, choroba: str = ""):
        self.apatia = apatia
        self.bol_w_klatce = bol_w_klatce
        self.goraczka = goraczka
        self.kaszel = kaszel
        self.flegma = flegma
        self.krwioplucie = krwioplucie
        self.nocne_poty = nocne_poty
        self.obrzek_nog = obrzek_nog
        self.sennosc = sennosc
        self.sinica = sinica
        self.splycenie_oddechu = splycenie_oddechu
        self.suchosc_w_ustach = suchosc_w_ustach
        self.swiszczacy_oddech = swiszczacy_oddech
        self.szybkie_bicie_serca = szybkie_bicie_serca
        self.utrata_wagi = utrata_wagi
        self.utrudnione_oddychanie = utrudnione_oddychanie
        self.zawroty_glowy = zawroty_glowy
        self.zmeczenie = zmeczenie
        self.zmniejszony_apetyt = zmniejszony_apetyt
        self.dusznosc = dusznosc
        self.choroba = choroba
        self.symptoms = self.toList()

    def toList(self) -> []:
        l = [self.apatia, self.bol_w_klatce, self.goraczka, self.kaszel, self.flegma, self.krwioplucie, self.nocne_poty,
             self.obrzek_nog, self.sennosc, self.sinica, self.splycenie_oddechu, self.suchosc_w_ustach,
             self.swiszczacy_oddech, self.szybkie_bicie_serca, self.utrata_wagi, self.utrudnione_oddychanie,
             self.zawroty_glowy, self.zmeczenie, self.zmniejszony_apetyt, self.dusznosc, self.choroba]
        if l[len(l) - 1] == "":
            l.pop(len(l) - 1)
        return l

    def __str__(self):
        for symptom in self.symptoms:
            print(symptom)
