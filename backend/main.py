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
                    # print('bij vraag', key)
                    # print('Dit is de sleutel', question)
                    # print('Dit is de waarde', content)
        # print('\n')
        # print('Inlezen succesvol')
        # print('dit zijn de antwoorden', antwoorden)
        # print('dit zijn de gewichten', gewichten)

        d = {'antwoorden': antwoorden, 'gewichten': gewichten}
        inputdata = pd.DataFrame(d)  # dataframe maken; handig voor doorzoeken
        Sys.make_recommendation(inputdata) #puntentoekenning
        x = Sys.give_top4() #top 4 eruit halen
        print('\n')
        print('Dit is de recommendation dat zal worden opgeslagen')
        print(x)
        ident = Sys.export_data(x) #schrijven het weg naar excel
        print('Dit is de bijhorende ticket voor de weggeschreven recommendations', ident)
        print('Response: \n')

        return {"id":ident}

    def give_recommendation(self, id):
        print('got here')
        data = Sys.read_data(id)
        return jsonify(data, 200, {'Access-Control-Allow-Origin': '*'})


@app.route('/get_id/', methods=['POST'])
def recommender():
    REST = RestAPI()
    print('Contact with frontend ok')
    print('\n')
    data = request.data
    # print('Dit is de raw data')
    # print(data)
    # print('----')
    # print('Dit is de json data')


    datastr= data.decode("utf-8")
    datajson= json.loads(datastr)
    #print(datajson)
    # print('---')
    # for key, value in datajson.items():
    #     print('Key', key)
    #     print('Keytype', type(key))
    #     print('\n')
    #     print('Value', value)
    #     print('Valuetype', type(value))
    #     print('\n')

    print(REST.give_id(datajson)) #zodat de recommendation gemaakt kunnen worden
    return {'id':1}
    #return REST.give_id(datajson)

@app.route('/get_recommendation/', methods=['GET'])
def test():
    REST = RestAPI()
    print('test binnengegaan')
    id = request.get_json()
    print(id)
    return REST.give_recommendation(id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)

#README: om het programma te testen moet je deze code runnen. dus run 'main'!

"""


Sys = R.Databank()
Sys.create_dog()

#OPM: dit is een test input en volledig fictief / Voor de meeste input zullen een paar honden dezelfde scores hebben, dit is normaal aangezien de dataset beperkt is en dus niet elke hond uniek
antwoorden = ['Reu', 'Eerder groot', 'Gouden senioren jaren (2014 en ouder)', 'Nee', 'Nee', 'Nee', 'Ja', 'Ja, knuffelkontjes!', 'Dat is voor mij niet zo belangrijk', 'Nee'] #Met deze antwoorden vind je Max en Sky
gewichten = [100, 50, 50, 50, 50, 100, 10, 80, 100, 50] #je kan spelen met de gewichten, 50 wilt zeggen neutraal.
d= {'antwoorden': antwoorden, 'gewichten': gewichten}
inputdata = pd.DataFrame(d)  # dataframe maken; handig voor doorzoeken



#We tabuleren de punten per hond met de gegeven inputdata:
Sys.make_recommendation(inputdata)


#We geven de data weer/output naar JSON

x=Sys.give_top4()
#print(x)
ident = Sys.export_data(x)
#Sys.read_data(140677493168464)
print(Sys.read_data(ident))


"""
