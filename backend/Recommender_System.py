#if you are commits behind master: checkout on branch, then pull into current merge from master origin (remote)


#Tip: if you are commits behind master (as seen on Github): checkout on branch (locally), then pull into current merge from master origin (remote)
# In order to update branch, checkout into branch (locally), pull into current merge from branch (remote)
import datetime as dt
import pandas as pd
import numpy as py
import pandas as pd
import Dog as D
import Recommender_System as R

class Databank:

    def __init__(self):
        self.__recommender = []  # lijst van reservaties maken; handig bij opvragen van gegevens
        self.__recommender_data = pd.DataFrame(columns=['dog_id', 'name', 'sex', 'size', 'age', 'dogfriendly', 'petfriendly','childfriendly','gardenreq','hug','training','BCD','Description','image','score'])  # dataframe maken; handig voor doorzoeken

    def create_dog(self):

        df = pd.read_csv("Dogsnew" + '.csv', nrows=10000)  # data inlezen
        for row, dog in df.iterrows():  # .itterrows() geeft een rowindex en data weer in de rij
            groep9.append_dog_data(row, dog['Naam'], dog['Geslacht'], dog['Groot'], dog['Leeftijd'],
                                   dog['Andere_hond'],
                                   dog['Andere_dieren'], dog['Kinderen'], dog['Tuin'], dog['Knuffelbeer'],
                                   dog['Training_sport'], dog['BCDp'], dog['Beschrijving'], dog['Image'])

    def append_dog_data(self, id, name, sex, size, age, dogfriendly, catfriendly, childfriendly, gardenreq, hug, training, BCD, Description, image, score= 0):


        nieuwe_hond = D.Dog(id, name, size, sex, age, dogfriendly, catfriendly, childfriendly, gardenreq, hug, training, BCD, Description, image)

        self.__recommender.append(nieuwe_hond)
        self.__recommender_data = self.__recommender_data.append({'dog_id': id, 'name': name, 'size': size, 'sex': sex,
             'age': age, 'dogfriendly': dogfriendly, 'catfriendly': catfriendly, 'childfriendly': childfriendly,'gardenreq': gardenreq,
             'hug': hug,'training': training,'BCD': BCD,'score': score,'Description': Description, 'image': image}, ignore_index=True)



    def add_points(self, id, score):
        for row, dog in self.__recommender_data.iterrows():  # .itterrows() geeft een rowindex en data weer in de rij
            if dog['dog_id'] == id:
                self.__recommender_data.loc[row, 'score']+= score

    def give_id(self, naam):
        df = self.__recommender_data
        for row, dog in df.iterrows():  # .itterrows() geeft een rowindex en data weer in de rij
            if dog['name'] == naam:
                return df.loc[row, 'dog_id']

    def give_dog_name(self, id):
        df = self.__recommender_data
        for row, dog in df.iterrows():  # .itterrows() geeft een rowindex en data weer in de rij
            if dog['dog_id'] == id:
                return df.loc[row, 'name']

    def give_all(self):
        for row, dog in self.__recommender_data.iterrows():  # .itterrows() geeft een rowindex en data weer in de rij
            self.__recommender_data.loc[row, 'score']+= 1

    def give_dog_data(self, naam):
        df = self.__recommender_data
        for row, dog in df.iterrows():  # .itterrows() geeft een rowindex en data weer in de rij
            if dog['name'] == naam:
                return df.loc[row, :]

    def give_data(self):
        return self.__recommender_data

    def give_score(self):
        return self.__recommender_data['score']

    def give_top4(self):
        df = self.__recommender_data
        return df.sort_values(by=['score'], ascending=False).head(4)

    def search_dupl(self):

        for row1, dog1 in self.__recommender_data.iterrows():  # .itterrows() geeft een rowindex en data weer in de rij
            count =1
            for row2, dog2 in self.__recommender_data.iterrows():
                if row1==row2:
                    break
                else:
                    if dog1['name']== dog2['name']:
                        count+=1
                        print('Voor', dog1['name'], 'hebben we exact', count, "exemplar(en) gevonden")





groep9 = Databank()
groep9.create_dog()


inputdata = {'Teef':80, 'Middelmaatje':58, 'Eerder jong (2020 en jonger)':100, 'Ja, een reu':20, 'Ja':12, 'Enkel kinderen boven 12 jaar':0, 'Onbekend':100, 'Onbekend':80, 'Ja':0, 'Ja':50}



#onze recommender
for input, gewicht in inputdata.items():
    for row, dog in groep9.give_data().iterrows(): #we gaan door elke hond in onze database
        if dog['sex'] == input: #V1: We willen absoluut de juiste geslacht honden, daarom 2 als basis
            groep9.add_points(dog['dog_id'], 2 + ((gewicht - 50) / 50))
        if dog['size'] == input: #V2: We willen ook zeker de juiste grootte, maar minder belangrijk dan geslacht
            groep9.add_points(dog['dog_id'], 1.5 + ((gewicht - 50) / 50))
        if dog['age'] == input: #V3: Gewicht beslissen mensen zelf
            groep9.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))
        if dog['dogfriendly'] == input: #V4
            groep9.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))
        if dog['petfriendly'] == input: #V5
            groep9.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))

# -------- Vragen met speciale Jackie logica komt hieronder

        if dog['childfriendly'] == input and input == "Nee": #V6 als er dus enkel volwassene zijn krijgt iedereen een punt, oftewel niemand
            continue
        if dog['childfriendly'] == input and input == "Enkel kinderen boven 12 jaar":  # V6 als er dus enkel volwassene zijn krijgt iedereen een punt, oftewel niemand
            groep9.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))

#--------

        if dog['gardenreq'] == input and input == "Onbekend": #V7, indien input "nee" dan enkel honden met
            groep9.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))
        if dog['gardenreq'] == input and input == "Ja": #V7, indien input "ja" dan alle honden een punt, equivalent als zeggen dat niemand iets krijgt.
            continue
# --------

        if dog['hug'] == input and input == "Ja": #V8
            groep9.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))
        if dog['hug'] == input and input == "Onbekend": #V8
           continue

# --------

        if dog['training'] == input and input == "Ja":  # V8
            groep9.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))
        if dog['training'] == input and input == "Onbekend":  # V8
            continue

#--------
        if dog['BCD'] == input and input == "Ja": #V10
            groep9.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))
        if dog['BCD'] == input and input == "Nee": #V10
            continue

print('Dit zijn de beste honden gegeven uw antwoorden: ')
print('\n')
print(groep9.give_top4())
print('The end')
print('Duplicates: ')
print('\n')
#groep9.search_dupl()
