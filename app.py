#http://127.0.0.1:5000/apidocs

from flask import flask, jsonify, request, Flask
from flasgger import swag_from, Swagger

from Classifiers.Classifire import Classifire
from Database.DatabaseConnection import DatabaseConnection
from Models.Symptoms import Symptoms

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    """
    Diagnose a patient based on symptoms
    ---
    tags:
      - diagnosis
    parameters:
      - in: query
        name: apatia
        type: string
        required: true
      - in: query
        name: bol_w_klatce
        type: string
        required: true
      - in: query
        name: goraczka
        type: string
        required: true
      - in: query
        name: kaszel
        type: string
        required: true
      - in: query
        name: flegma
        type: string
        required: true
      - in: query
        name: krwioplucie
        type: string
        required: true
      - in: query
        name: nocne_poty
        type: string
        required: true
      - in: query
        name: obrzęk_nog
        type: string
        required: true
      - in: query
        name: sennosc
        type: string
        required: true
      - in: query
        name: sinica
        type: string
        required: true
      - in: query
        name: splycenie_oddechu
        type: string
        required: true
      - in: query
        name: suchosc_w_ustach
        type: string
        required: true
      - in: query
        name: swiszczacy_oddech
        type: string
        required: true
      - in: query
        name: szybkie_bicie_serca
        type: string
        required: true
      - in: query
        name: utrata_wagi
        type: string
        required: true
      - in: query
        name: utrudnione_oddychanie
        type: string
        required: true
      - in: query
        name: zawroty_glowy
        type: string
        required: true
      - in: query
        name: zmeczenie
        type: string
        required: true
      - in: query
        name: zmniejszony_apetyt
        type: string
        required: true
         - in: query
        name: dusznosc
        type: string
        required: true
    responses:
      200:
        description: successful operation
        schema:
          type: object
          properties:
            diagnosis:
              type: string
    """

    apatia = request.args.get('apatia')
    bol_w_klatce = request.args.get('bol_w_klatce')
    goraczka = request.args.get('goraczka')
    kaszel = request.args.get('kaszel')
    flegma = request.args.get('kaszel_z_flegma')
    krwioplucie = request.args.get('krwioplucie')
    nocne_poty = request.args.get('nocne_poty')
    obrzek_nog = request.args.get('obrzęk_nog')
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
    dusznosc=request.args.get('dusznosc')

    for symptom, value in apatia, bol_w_klatce, goraczka, kaszel, flegma, krwioplucie, nocne_poty, obrzek_nog, sennosc, sinica, splycenie_oddechu, suchosc_w_ustach, swiszczacy_oddech, szybkie_bicie_serca, utrata_wagi, utrudnione_oddychanie, zawroty_glowy, zmeczenie, zmniejszony_apetyt:
        if not validate_symptom(value):
            return jsonify({"error": f"Invalid value for {symptom}"}), 400

    symptoms = Symptoms(apatia, bol_w_klatce, goraczka, kaszel, flegma, krwioplucie, nocne_poty, obrzek_nog, sennosc,
                        sinica, splycenie_oddechu, suchosc_w_ustach, swiszczacy_oddech, szybkie_bicie_serca,
                        utrata_wagi, utrudnione_oddychanie, zawroty_glowy, zmeczenie, zmniejszony_apetyt, dusznosc, "")
    print(symptoms.apatia)

    base = DatabaseConnection()
    map_poidCh: {} = base.map_poidCh
    classifire = Classifire(symptoms, map_poidCh)





    # Przetwarzanie objawów i diagnoza
    diagnosis = "Sample Diagnosis"
    return jsonify({"diagnosis": diagnosis})


def validate_symptom(symptom):
    valid_values = {"tak", "nie", "czasami"}
    if symptom not in valid_values:
        return False
    return True

if __name__ == '__main__':
    app.run(debug=True)
