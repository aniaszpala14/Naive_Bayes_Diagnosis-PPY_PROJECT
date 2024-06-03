from Models.Symptoms import Symptoms


class Classifire():
    given = None
    map_poidCh = None

    def __init__(self, given: Symptoms, map_poidCh: {}):
        self.given = given
        self.map_poidCh = map_poidCh

    def train(self):

        pass

    def classify(self):
        pass


