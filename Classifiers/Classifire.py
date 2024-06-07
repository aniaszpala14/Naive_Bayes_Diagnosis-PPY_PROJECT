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

    def __init__(self, given: Symptoms, map_poidCh: {}, training: []):
        self.given = given
        self.map_poidCh = map_poidCh
        self.training = pd.DataFrame(training)
        print(self.training)
        print("gdsdgjdfasd")



    def train(self):
        pass


    def classify(self):
        pass


