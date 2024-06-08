from Database.DatabaseConnection import DatabaseConnection
from Models.Symptoms import Symptoms
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import pandas as pd

iris = datasets.load_iris()
X = iris.data
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25)


class Classifire():
    given: []
    map_poidCh: {}
    training: pd.DataFrame
    model: GaussianNB

    def __init__(self, given: Symptoms, map_poidCh: {}, training: [[]]):
        self.given = given.symptoms
        self.map_poidCh = map_poidCh
        self.training = pd.DataFrame(training, columns=["apatia", "bol_w_klatce", "goraczka", "kaszel", "flegma", "krwioplucie", "nocne_poty",
             "obrzek_nog", "sennosc", "sinica", "splycenie_oddechu", "suchosc_w_ustach",
             "swiszczacy_oddech", "szybkie_bicie_serca", "utrata_wagi", "utrudnione_oddychanie",
             "zawroty_glowy", "zmeczenie", "zmniejszony_apetyt", "dusznosc", "choroba"])
        print(self.training)
        self.train()


    def train(self):
        X = self.training.loc[:, "apatia":"dusznosc"]
        Y = self.training.loc[:, "choroba"]
        scale_mapper = {"Tak": 1, "Czasami": 2, "Nie": 3}
        pd.set_option('future.no_silent_downcasting', True)
        for column in X.columns:
            X[column] = X[column].map(scale_mapper)
        X = X.astype(float)
        print(X)
        print(Y)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25)
        self.model = GaussianNB()
        self.model.fit(X_train, Y_train)
        print(self.model.score(X_test, Y_test))



    def classify(self) -> str:
        print(self.given)

        scale_mapper = {"tak": 1, "czasami": 2, "nie": 3}
        given = [scale_mapper.get(symptom, 0) for symptom in self.given]
        print(given)
        prediction = self.model.predict(pd.DataFrame(given))
        return self.map_poidCh.get(prediction)


