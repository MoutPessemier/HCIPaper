import Recommender_System as R
import pandas as pd
from flask import Flask, jsonify, request


# Test it with this command in terminal:
# curl -X POST http://localhost:5001/recommender -H 'Content-Type: application/json' -d '{"answers": [ {"answer": "Teef", "weight": 100 }, {"answer": "Eerder klein", "weight": 100 }, {"answer": "Gouden senioren jaren (2014 en ouder)", "weight": 100 }, {"answer": "Ja, een reu", "weight": 100 }, {"answer": "Nee", "weight": 100 }, {"answer": "Enkel kinderen boven 12 jaar", "weight": 100 }, {"answer": "Ja", "weight": 100 }, {"answer": "Ja, knuffelkontjes!", "weight": 100 }, {"answer": "Dat is voor mij niet zo belangrijk", "weight": 100 }, {"answer": "Nee", "weight": 100 } ]}'

app = Flask(__name__)
Sys = R.Databank()
Sys.create_dog()

class RestAPI:

    def give_id(self, data):
        # System setup
        print('in post')
        antwoorden = []
        gewichten = []

        for x in data['answers']: #parsing moet nog aangepast worden

            antwoorden.append(x["answer"])
            gewichten.append(x["weight"])

        d = {'antwoorden': antwoorden, 'gewichten': gewichten}
        inputdata = pd.DataFrame(d)  # dataframe maken; handig voor doorzoeken
        Sys.make_recommendation(inputdata) #puntentoekenning
        x = Sys.give_top4() #top 4 eruit halen
        ident = Sys.export_data(x) #schrijven het weg naar excel

        return jsonify(ident, 200, {'Access-Control-Allow-Origin': '*'})

    def give_recommendation(self, id):
        print('got here')
        data = Sys.read_data(id)
        return jsonify(data, 200, {'Access-Control-Allow-Origin': '*'})


@app.route('/get_id/', methods=['POST'])
def recommender():
    REST = RestAPI()
    print('recommender binnengegaan')
    data = request.data
    print('Dit is de inkomende data', data)
    return REST.give_id(data)

@app.route('/get_recommendation/', methods=['GET'])
def test():
    REST = RestAPI()
    print('test binnengegaan')
    id = request.data
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