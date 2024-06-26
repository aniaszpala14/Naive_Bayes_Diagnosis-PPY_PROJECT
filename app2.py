'''
from flask import Flask, request, render_template

from Classifiers.Classifire import Classifire
from Database.DatabaseConnection import DatabaseConnection
from Models.Symptoms import Symptoms

app2 = Flask(__name__)


@app2.route('/')
def index():
    return render_template('index.html')




@app2.route('/submit', methods=['GET'])
def submit():
    apatia = request.args.get('apatia')
    bol_w_klatce = request.args.get('bol_w_klatce')
    goraczka = request.args.get('goraczka')
    kaszel = request.args.get('kaszel')
    flegma = request.args.get('kaszel_z_flegma')
    krwioplucie = request.args.get('krwioplucie')
    nocne_poty = request.args.get('nocne_poty')
    obrzek_nog = request.args.get('obrzek_nog')
    sennosc = request.args.get('sennosc')
    sinica = request.args.get('sinica')
    splycenie_oddechu = request.args.get('splycenie_oddechu')
    suchosc_w_ustach = request.args.get('suchosc_w_ustach')
    swiszczacy_oddech = request.args.get('swiszczacy_oddech')
    szybkie_bicie_serca = request.args.get('szybkie_bicie_serca')
    utrata_wagi = request.args.get('utrata_wagi')
    utrudnione_oddychanie = request.args.get('utrudnione_oddychanie')
    zawroty_glowy = request.args.get('zawroty_glowy')
    zmeczenie = request.args.get('zmeczenie')
    zmniejszony_apetyt = request.args.get('zmniejszony_apetyt')
    dusznosc = request.args.get('dusznosc')
    print(suchosc_w_ustach)

    for value in apatia, bol_w_klatce, goraczka, kaszel, flegma, krwioplucie, nocne_poty, obrzek_nog, sennosc, sinica, splycenie_oddechu, suchosc_w_ustach, swiszczacy_oddech, szybkie_bicie_serca, utrata_wagi, utrudnione_oddychanie, zawroty_glowy, zmeczenie, zmniejszony_apetyt:
        if not validate_symptom(value):
            return ({"error": f"Invalid value for {value}"}), 400

    symptoms = Symptoms(apatia, bol_w_klatce, goraczka, kaszel, flegma, krwioplucie, nocne_poty, obrzek_nog,
                            sennosc,
                            sinica, splycenie_oddechu, suchosc_w_ustach, swiszczacy_oddech, szybkie_bicie_serca,
                            utrata_wagi, utrudnione_oddychanie, zawroty_glowy, zmeczenie, zmniejszony_apetyt, dusznosc,
                            "")


    base = DatabaseConnection()
    classifire = Classifire(symptoms, base)


    wynik = classifire.classify()
    base.close_connection()
    return render_template('result.html', wynik=wynik)


def validate_symptom(symptom):
    valid_values = {"tak", "nie", "czasami"}
    if symptom not in valid_values:
        return False
    return True


if __name__ == '__main__':
    app2.run(debug=True)
'''