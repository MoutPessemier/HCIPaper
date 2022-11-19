import Recommender_System as R
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import datetime as dt

#TODO: Endpoint maken zodat de onderzoeksvragen kunnen worden opgeslaan
#TODO: Timestamps verwerken naar excel


app = Flask(__name__)
CORS(app)
Sys = R.Databank()
Sys.create_dog()

class RestAPI:

    def give_id(self, data):

        antwoorden = []
        gewichten = []

        for key1, value in data.items():
            if key1 == "startTime" or key1 == "endTime":
                continue #later bijhouden

            else:
                for key2, content in value.items():
                    if key2 == 'value':
                        antwoorden.append(content)
                    if key2 == 'weight':
                        gewichten.append(content)

        d = {'antwoorden': antwoorden, 'gewichten': gewichten}
        inputdata = pd.DataFrame(d)  # dataframe maken; handig voor doorzoeken
        Sys.make_recommendation(inputdata) #puntentoekenning
        x = Sys.give_top4() #top 4 eruit halen
        ident = Sys.export_excel(x) #schrijven het weg naar excel

        return {"id":ident}

    def give_recommendation(self, id):
        for values in id.values():
            data = Sys.read_excel(values)
        return {"recommendations": data}


@app.route('/get_id/', methods=['POST'])
def recommender():
    REST = RestAPI()
    data = request.data
    datastr= data.decode("utf-8")
    datajson= json.loads(datastr)

    return REST.give_id(datajson)

@app.route('/get_recommendation/', methods=['GET'])
def test():
    REST = RestAPI()
    print('test binnengegaan')
    id = json.loads(request.data.decode("utf-8"))
    print(id)
    return REST.give_recommendation(id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)


