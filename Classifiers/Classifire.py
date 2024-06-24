from Database import DatabaseConnection
from Models.Symptoms import Symptoms
import pandas as pd
import pickle
from sklearn.naive_bayes import GaussianNB


class Classifire:
    given: []
    map_poidch: {}
    training: pd.DataFrame
    model: GaussianNB
    base: DatabaseConnection

    def __init__(self, given: Symptoms, map_poidch: {}, base: DatabaseConnection):
        self.given = given.symptoms
        self.map_poidCh = map_poidch
        self.base = base
        self.classify()

    def train(self):
        self.training = pd.DataFrame(self.base.przypadkiToLIst(),
                                     columns=["apatia", "bol_w_klatce", "goraczka", "kaszel", "flegma", "krwioplucie",
                                              "nocne_poty",
                                              "obrzek_nog", "sennosc", "sinica", "splycenie_oddechu",
                                              "suchosc_w_ustach",
                                              "swiszczacy_oddech", "szybkie_bicie_serca", "utrata_wagi",
                                              "utrudnione_oddychanie",
                                              "zawroty_glowy", "zmeczenie", "zmniejszony_apetyt", "dusznosc",
                                              "choroba"])
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
        cur = self.base.con.cursor()
        cur.execute('SELECT 1 FROM models WHERE name = "GaussianNB"')
        model_exists = cur.fetchone()[0] > 0

        if model_exists:
            cur.execute('SELECT model FROM models WHERE name = "GaussianNB"')
            serialized_model = cur.fetchone()[0]

            self.model = pickle.loads(serialized_model)
        else:
            serialized_model = pickle.dumps(self.model)
            cur.execute('''
                INSERT INTO models (name, model) VALUES ('GaussianNB', serialized_model)''')

        self.base.commit()
        self.base.closeConnection()

        scale_mapper = {"tak": 1, "czasami": 2, "nie": 3}
        given = [scale_mapper.get(symptom, 0) for symptom in self.given]
        prediction = self.model.predict(pd.DataFrame([given]))
        return self.map_poidCh.get(prediction[0])
