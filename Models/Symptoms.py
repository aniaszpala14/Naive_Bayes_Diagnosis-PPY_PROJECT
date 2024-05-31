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
    kaszel_z_flegma: str
    obrzek_nog: str
    suchosc_w_ustach: str
    zmniejszony_apetyt: str
    utrudnione_oddychanie: str
    szybkie_bicie_serca: str
    sennosc_w_dzien: str
    zawroty_glowy: str

    def __init__(self, apatia: str, bol_w_klatce: str, goraczka: str, kaszel: str, kaszel_z_flegma: str,
                 krwioplucie: str, nocne_poty: str, obrzek_nog: str, sennosc_w_dzien: str, sinica: str,
                 splycenie_oddechu: str, suchosc_w_ustach: str, swiszczacy_oddech: str, szybkie_bicie_serca: str,
                 utrata_wagi: str, utrudnione_oddychanie: str, zawroty_glowy: str, zmeczenie: str,
                 zmniejszony_apetyt: str):
        self.apatia = apatia
        self.bol_w_klatce = bol_w_klatce
        self.goraczka = goraczka
        self.kaszel = kaszel
        self.kaszel_z_flegma = kaszel_z_flegma
        self.krwioplucie = krwioplucie
        self.nocne_poty = nocne_poty
        self.obrzek_nog = obrzek_nog
        self.sennosc_w_dzien = sennosc_w_dzien
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
