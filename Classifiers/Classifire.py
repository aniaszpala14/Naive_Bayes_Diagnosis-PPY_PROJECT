from Database import DatabaseConnection
from Models.Symptoms import Symptoms
import pandas as pd
import pickle
from sklearn.naive_bayes import GaussianNB


class Classifire:
    given: []
    map_by_idch: {}
    training: pd.DataFrame
    model: GaussianNB
    base: DatabaseConnection

    def __init__(self, given: Symptoms, base: DatabaseConnection):
        self.given = given.symptoms
        self.base = base
        self.map_by_idch = self.base.map_by_idch
        self.classify()

    def train(self):
        self.training = pd.DataFrame(self.base.cases_to_list(),
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
        model_exists = self.base.is_model_in_database()

        if model_exists:
            serialized_model = self.base.get_model()
            self.model = pickle.loads(serialized_model)
        else:
            self.train()
            serialized_model = pickle.dumps(self.model)
            self.base.add_model(serialized_model)

        self.base.commit()

        scale_mapper = {"tak": 1, "czasami": 2, "nie": 3}
        given = [scale_mapper.get(symptom, 0) for symptom in self.given]
        prediction = self.model.predict(pd.DataFrame([given]))
        return self.map_by_idch.get(prediction[0])
