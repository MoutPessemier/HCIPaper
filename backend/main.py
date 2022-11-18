import Recommender_System as R
import pandas as pd
from flask import Flask, jsonify, request

# Test it with this command in terminal:
# curl -X POST http://localhost:5001/recommender -H 'Content-Type: application/json' -d '{"answers": [ {"answer": "Teef", "weight": 100 }, {"answer": "Eerder klein", "weight": 100 }, {"answer": "Gouden senioren jaren (2014 en ouder)", "weight": 100 }, {"answer": "Ja, een reu", "weight": 100 }, {"answer": "Nee", "weight": 100 }, {"answer": "Enkel kinderen boven 12 jaar", "weight": 100 }, {"answer": "Ja", "weight": 100 }, {"answer": "Ja, knuffelkontjes!", "weight": 100 }, {"answer": "Dat is voor mij niet zo belangrijk", "weight": 100 }, {"answer": "Nee", "weight": 100 } ]}'

app = Flask(__name__)

class RestAPI:

    def make_json(self, dataframe):
        #dict = {"id": [], "name": [], "description": [], "image": []}
        ddic = {}
        for row, dog in dataframe.iterrows():

            # dict['id'].append(dog["dog_id"])
            # dict['name'].append(dog["name"])
            # dict['description'].append(dog["description"])
            # dict['image'].append(dog["image"])
            ddic[dog['name']] = dog["description"]


        return ddic

    def post(self, jsonObject):
        # System setup
        print('in post')
        antwoorden = []
        gewichten = []

        for x in jsonObject['answers']:

            antwoorden.append(x["answer"])
            gewichten.append(x["weight"])

        d = {'antwoorden': antwoorden, 'gewichten': gewichten}
        inputdata = pd.DataFrame(d)  # dataframe maken; handig voor doorzoeken
        Sys.make_recommendation(inputdata)

        return jsonify(self.make_json(Sys.give_top4())), 200, {'Access-Control-Allow-Origin': '*'}

    def get(self):
        print('got here')
        return {'res': "hey, Nam"}, 200, {'Access-Control-Allow-Origin': '*'}


@app.route('/recommender/', methods=['POST'])
def recommender():
    Sys = R.Databank()
    Sys.create_dog()
    REST = RestAPI()
    print('recommender binnengegaan')
    data = request.get_json()
    print('Dit is de inkomende data', data)
    return 'ok'

@app.route('/test/', methods=['GET'])
def test():
    REST = RestAPI()
    print('test binnengegaan')
    return REST.get()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)

#README: om het programma te testen moet je deze code runnen. dus run 'main'!



"""
Sys = R.Databank()
Sys.create_dog()
#TODO: Inlezing van data via JSON
#OPM: dit is een test input en volledig fictief / Voor de meeste input zullen een paar honden dezelfde scores hebben, dit is normaal aangezien de dataset beperkt is en dus niet elke hond uniek
antwoorden = ['Reu', 'Eerder groot', 'Gouden senioren jaren (2014 en ouder)', 'Nee', 'Nee', 'Nee', 'Ja', 'Ja, knuffelkontjes!', 'Dat is voor mij niet zo belangrijk', 'Nee'] #Met deze antwoorden vind je Max en Sky
gewichten = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50] #je kan spelen met de gewichten, 50 wilt zeggen neutraal.
d= {'antwoorden': antwoorden, 'gewichten': gewichten}
inputdata = pd.DataFrame(d)  # dataframe maken; handig voor doorzoeken



#We tabuleren de punten per hond met de gegeven inputdata:
Sys.make_recommendation(inputdata)

#TODO: output naar JSON schrijven
#We geven de data weer/output naar JSON
print('\n')
print('Dit zijn de beste honden gegeven uw antwoorden: ') #Dit is slechts een test
print('\n')
print(Sys.give_top4())
print('\n')
print('The end')
"""

#TODO: Recommendation oplsaan met een ID bij eerste request. Bij tweede request via ID dezelfde recommendation teruggeven.