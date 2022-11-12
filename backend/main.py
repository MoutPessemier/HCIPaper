import Recommender_System as R
import pandas as pd
from flask import Flask

from flask import request
from flask_restful import Resource, Api, reqparse

#Dit is de REST API
"""
app = Flask(__name__)
@app.route('/recommendations')

@app.route('/hello')
def index(input):
    return "Hello " + input
if __name__ == "__main__":
    app.run()
"""

#README: om het programma te testen moet je deze code runnen. dus run 'main'!



#System setup
Sys = R.Databank()
Sys.create_dog()

#TODO: Inlezing van data via JSON
#OPM: dit is een test input en volledig fictief / Voor de meeste input zullen een paar honden dezelfde scores hebben, dit is normaal aangezien de dataset beperkt is en dus niet elke hond uniek
antwoorden = ['Teef', 'Eerder klein', 'Gouden senioren jaren (2014 en ouder)', 'Ja', 'Nee', 'Enkel kinderen boven 12 jaar', 'Ja', 'Ja, knuffelkontjes!', 'Dat is voor mij niet zo belangrijk', 'Nee'] #Met deze antwoorden vind je Max en Sky
gewichten = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100] #je kan spelen met de gewichten, 50 wilt zeggen neutraal.
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
