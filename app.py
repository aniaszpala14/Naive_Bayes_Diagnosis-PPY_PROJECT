import time

from flask import Flask, request, render_template, redirect, url_for
from confluent_kafka import Producer, Consumer, KafkaException
import threading
import json

from Classifiers.Classifire import Classifire
from Database.DatabaseConnection import DatabaseConnection
from Models.Symptoms import Symptoms

app = Flask(__name__)

p = Producer({'bootstrap.servers': 'localhost:9092'})
base = DatabaseConnection()


def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')


@app.route('/')
def description():
    return render_template('description.html')


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/submit', methods=['GET'])
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

    data = symptoms.to_dict()
    p.produce('my_topic', value=json.dumps(data), callback=delivery_report)

    p.flush()

    consumer_thread = threading.Thread(target=consume)
    consumer_thread.start()

    return redirect(url_for('result'))


@app.route('/result')
def result():
    while result is None:
        time.sleep(1)
    return render_template('result.html', wynik=result)


def consume():
    c = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'my_group',
        'auto.offset.reset': 'earliest'
    })
    c.subscribe(['my_topic'])

    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        else:
            print(f'Received message: {msg.value().decode("utf-8")}')

            data = json.loads(msg.value().decode("utf-8"))
            symp = Symptoms(data)
            classifire = Classifire(symp, base)
            wynik = classifire.classify()

            global result
            result = wynik
            # Przekierowanie do strony z wynikiem
        # return render_template('result.html', wynik=wynik)


def validate_symptom(symptom):
    valid_values = {"tak", "nie", "czasami"}
    if symptom not in valid_values:
        return False
    return True


if __name__ == '__main__':
    app.run(debug=True)

# bin\windows\zookeeper-server-start.bat config\zookeeper.properties
# bin\windows\kafka-server-start.bat config\server.properties
# jps
