import Recommender_System as R
import pandas as pd
from flask import Flask, request
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
        dogs = Sys.read_excel(int(id))
        return {"recommendations": dogs}

    def export_research_question(self, data):
        ID = 0
        V1 = 0
        V2 = 0
        V3 = 0
        finalTime = 0
        entry = []
        for key1, value in data.items():

            if key1 == "finalTime":
                finalTime = value
            if key1 == "ID":
                ID = int(value)
            if key1 == "Q1":
                V1 = value
            if key1 == "Q2":
                V2 = value
            if key1 == "Q3":
                V3 = value


        entry.append(V1)
        entry.append(V2)
        entry.append(V3)
        entry.append(finalTime)
        Sys.find_and_export(ID, entry)

        return {"Message:": "Entry Saved"}


@app.route('/getId', methods=['POST'])
def getID():
    REST = RestAPI()
    data = request.get_json()
    return REST.give_id(data)

@app.route('/getRecommendation', methods=['GET'])
def getRecommendations():
    REST = RestAPI()
    args = request.args
    id = args.get('id')
    return REST.give_recommendation(id)

@app.route('/giveResearch', methods=['POST'])
def insert_question():
    REST = RestAPI()
    data = request.get_json()
    return REST.export_research_question(data)

@app.route('/wakeUp')
def wakeup():
    return {'status': 'OK'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)


