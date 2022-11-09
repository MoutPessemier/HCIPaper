import Recommender_System as R
import pandas as pd


#REST API komt ook hier

#System setup
Sys = R.Databank()
Sys.create_dog()

#TODO: Inlezing van data via JSON
#OPM: dit is een test input en volledig fictief
antwoorden = ['Teef', 'Eerder klein', 'Gouden senioren jaren (2014 en ouder)', 'Nee', 'Nee', 'Enkel kinderen boven 12 jaar', 'Ja', 'Ja, knuffelkontjes!', 'Dat is voor mij niet zo belangrijk', 'Nee'] #Met deze antwoorden vind je Max en Sky
gewichten = [100, 50, 50, 50, 50, 50, 50, 50, 50, 50] #je kan spelen met de gewichten, 50 wilt zeggen neutraal.
d= {'antwoorden': antwoorden, 'gewichten': gewichten}
inputdata = pd.DataFrame(d)  # dataframe maken; handig voor doorzoeken



#We tabuleren de punten per hond met de gegeven inputdata:
Sys.make_recommendation(inputdata)

#TODO: output naar JSON schrijven
#We geven de data weer/output naar JSON
print('Dit zijn de beste honden gegeven uw antwoorden: ') #Dit is slechts een test
print('\n')
print(Sys.give_top4())
print('The end')
print('\n')