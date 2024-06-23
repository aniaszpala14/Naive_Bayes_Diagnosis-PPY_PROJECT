from Models.Symptoms import Symptoms
from sklearn.naive_bayes import GaussianNB
import pandas as pd


class Classifire:
    given: []
    map_poidch: {}
    training: pd.DataFrame
    model: GaussianNB

    def __init__(self, given: Symptoms, map_poidch: {}, training: [[]]):
        self.given = given.symptoms
        self.map_poidCh = map_poidch
        self.training = pd.DataFrame(training,
                                     columns=["apatia", "bol_w_klatce", "goraczka", "kaszel", "flegma", "krwioplucie",
                                              "nocne_poty",
                                              "obrzek_nog", "sennosc", "sinica", "splycenie_oddechu",
                                              "suchosc_w_ustach",
                                              "swiszczacy_oddech", "szybkie_bicie_serca", "utrata_wagi",
                                              "utrudnione_oddychanie",
                                              "zawroty_glowy", "zmeczenie", "zmniejszony_apetyt", "dusznosc",
                                              "choroba"])
        print(self.training)
        self.train()

    def train(self):
        x = self.training.loc[:, "apatia":"dusznosc"]
        y = self.training.loc[:, "choroba"]
        scale_mapper = {"Tak": 1, "Czasami": 2, "Nie": 3}
        pd.set_option('future.no_silent_downcasting', True)
        for column in x.columns:
            x[column] = x[column].map(scale_mapper)
        x = x.astype(float)
        self.model = GaussianNB()
        self.model.fit(x, y)

    def classify(self) -> str:
        scale_mapper = {"tak": 1, "czasami": 2, "nie": 3}
        given = [scale_mapper.get(symptom, 0) for symptom in self.given]
        prediction = self.model.predict(pd.DataFrame([given]))
        return self.map_poidCh.get(prediction[0])
