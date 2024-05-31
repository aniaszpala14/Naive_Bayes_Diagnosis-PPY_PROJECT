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
      - in: body
        name: body
        description: Patient symptoms
        required: true
        schema:
          type: object
          properties:
            kaszel:
              type: string
            dusznosc:
              type: string
            bol_w_klatce:
              type: string
            goraczka:
              type: string
            swiszczacy_oddech:
              type: string
            utrata_wagi:
              type: string
            zmeczenie:
              type: string
            krwioplucie:
              type: string
            nocne_poty:
              type: string
            splycenie_oddechu:
              type: string
            sinica:
              type: string
            apatia:
              type: string
            kaszel_z_flegma:
              type: string
            obrzęk_nog:
              type: string
            suchosc_w_ustach:
              type: string
            zmniejszony_apetyt:
              type: string
            utrudnione_oddychanie:
              type: string
            szybkie_bicie_serca:
              type: string
            sennosc_w_dzien:
              type: string
            zawroty_glowy:
              type: string
          example: {
              "kaszel": "Tak",
              "dusznosc": "Tak",
              "bol_w_klatce": "Tak",
              "goraczka": "Czasami",
              "swiszczacy_oddech": "Czasami",
              "utrata_wagi": "Tak",
              "zmeczenie": "Tak",
              "krwioplucie": "Tak",
              "nocne_poty": "Czasami",
              "splycenie_oddechu": "Tak",
              "sinica": "Tak",
              "apatia": "Tak",
              "kaszel_z_flegma": "Czasami",
              "obrzęk_nog": "Tak",
              "suchosc_w_ustach": "Nie",
              "zmniejszony_apetyt": "Tak",
              "utrudnione_oddychanie": "Tak",
              "szybkie_bicie_serca": "Czasami",
              "sennosc_w_dzien": "Czasami",
              "zawroty_glowy": "Tak"
          }
    responses:
      200:
        description: successful operation
        schema:
          type: object
          properties:
            diagnosis:
              type: string
    """
    data = request.json
    diagnosis = "Sample Diagnosis"
    return jsonify({"diagnosis": diagnosis})

if __name__ == '__main__':
    app.run(debug=True)