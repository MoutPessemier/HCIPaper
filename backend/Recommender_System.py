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

        df = pd.read_csv("Dogs" + '.csv', nrows=10000)  # data inlezen
        for row, dog in df.iterrows():  # .itterrows() geeft een rowindex en data weer in de rij
            groep9.append_dog_data(row, dog['Naam'], dog['Geslacht'], dog['Grootte'], dog['Leeftijd'],
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
        self.__recommender_data
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


print('----------')


groep9 = Databank()
groep9.create_dog()

# print('-----------')
# print(groep9.give_data())
# print('-----------')
#
# groep9.add_points(groep9.give_id('Bibi'), 23) #probleem is dat elke keer een nieuwe ID werd gegenereerd
# groep9.add_points(groep9.give_id('Bibi'), 14) #probleem is dat elke keer een nieuwe ID werd gegenereerd
# print(groep9.give_data())

inputdata = {'Rue':0, 'Middel':58, 'Jong':45, 'Rue':20, 'Nee':12, 'enkel volwassenen':0, 'Ja':100, 'onbelangrijk':80, 'Ja':0, 'Ja':0}

#V1,2,3 8,9,10 hebben een gewicht
#V4,5,6,7 hebben geen gewicht


#onze recommender
for input, gewicht in inputdata.items():
    for row, dog in groep9.give_data().iterrows(): #we gaan door elke hond in onze database
        if gewicht != 0:

            if input == dog['sex'] or input == dog['size'] or input == dog['age'] or input == dog['petfriendly']:
                groep9.add_points(dog['dog_id'], gewicht/50)

            if input == dog['dogfriendly']:
                groep9.add_points(dog['dog_id'], gewicht/50)

        else:
            groep9.add_points(dog['dog_id'], 1)



print('hello')
print('Dit zijn de beste honden gegeven uw antwoorden: ')
print('\n')
print(groep9.give_top4())
print('The end')


#print(groep9.give_dog_data('Marie'))