import Recommender_System as R
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
#
# http://localhost:1234/pages/formType1.html
# http://localhost:1234/pages/formType2.html
# http://localhost:1234/pages/formType3.html

#TODO: Endpoint maken zodat de onderzoeksvragen kunnen worden opgeslaan

app = Flask(__name__)
CORS(app)
Sys = R.Databank()
Sys.create_dog()

class RestAPI:

    def give_id(self, data):

        antwoorden = []
        gewichten = []
        startTime=0
        endTime=0
        formType=0
        questions = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"]

        for key1, value in data.items():

            if key1 == "startTime":
                startTime = value

            if key1 == "endTime":
                endTime = value

            if key1 == "formType":
                formType = value

            if key1 in questions:

                for key2, content in value.items():
                    if key2 == 'value':
                        antwoorden.append(content)
                    if key2 == 'weight':
                        gewichten.append(int(content))

        d = {'antwoorden': antwoorden, 'gewichten': gewichten}
        inputdata = pd.DataFrame(d)  # dataframe maken; handig voor doorzoeken
        x= Sys.make_recommendation(inputdata) #puntentoekenning
        x.append({'startTime':startTime})
        x.append({'endTime': endTime})
        x.append({'formType': formType})
        ident = Sys.export_excel(x) #schrijven het weg naar excel
        data_json= json.dumps({"id":ident})
        return data_json

    def give_recommendation(self, id):

        for values in id.values(): #assumption
            data = Sys.read_excel(values)
        return {"recommendations": data}

@app.route('/get_id/', methods=['POST'])
def recommender():
    REST = RestAPI()
    data = request.get_json()
    print(data)
    return REST.give_id(data)

@app.route('/get_recommendation/', methods=['GET'])
def getRecommendations():
    REST = RestAPI()
    id = json.loads(request.data.decode("utf-8"))
    print(id)
    return REST.give_recommendation(id)

@app.route('/wakeUp/')
def wakeup():
    return {'status': 'OK'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)


