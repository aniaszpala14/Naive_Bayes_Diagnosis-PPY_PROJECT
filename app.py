# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()

# http://127.0.0.1:5000/apidocs


from flask import Flask, jsonify, request
from flasgger import Swagger

from Models import Symptoms

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/diagnose', methods=['POST'])
def diagnose(apatia, bol_w_klatce, goraczka, kaszel, kaszel_z_flegma, krwioplucie, nocne_poty, obrzęk_nog, sennosc_w_dzien, sinica, splycenie_oddechu, suchosc_w_ustach, swiszczacy_oddech, szybkie_bicie_serca, utrata_wagi, utrudnione_oddychanie, zawroty_glowy, zmeczenie, zmniejszony_apetyt):
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
        name: kaszel_z_flegma
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
        name: sennosc_w_dzien
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
    responses:
      200:
        description: successful operation
        schema:
          type: object
          properties:
            diagnosis:
              type: string

    """
    # Przetwarzanie objawów i diagnoza
    diagnosis = "Sample Diagnosis"
    return jsonify({"diagnosis": diagnosis})


if __name__ == '__main__':
    app.run(debug=True)