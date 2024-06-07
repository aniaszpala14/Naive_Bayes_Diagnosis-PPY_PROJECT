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
    given = None
    map_poidCh = None
    training: pd.DataFrame

    def __init__(self, given: Symptoms, map_poidCh: {}, training: [[]]):
        self.given = given
        self.map_poidCh = map_poidCh
        self.training = pd.DataFrame(training, columns=["apatia", "bol_w_klatce", "goraczka", "kaszel", "flegma", "krwioplucie", "nocne_poty",
             "obrzek_nog", "sennosc", "sinica", "splycenie_oddechu", "suchosc_w_ustach",
             "swiszczacy_oddech", "szybkie_bicie_serca", "utrata_wagi", "utrudnione_oddychanie",
             "zawroty_glowy", "zmeczenie", "zmniejszony_apetyt", "dusznosc", "choroba"])
        print(self.training)
        X = self.training.loc[:, "apatia":"dusznosc"]
        Y = self.training.loc[:, "choroba"]
        print(X)
        print(Y)

    def train(self):
        pass


    def classify(self):
        pass


