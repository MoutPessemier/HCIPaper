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
            if row > len(df):
                break

            else:
                # print('\nRow number:', row)
                # print('Row-data:\n', dog)
                # print('The value of \'name\' in this row:', dog['name'])
                groep9.append_dog_data(id(dog['naam']), dog['Naam'], dog['Geslacht'], dog['Grootte'], dog['Leeftijd'],
                                       dog['Andere_hond'],
                                       dog['Andere_dieren'], dog['Kinderen'], dog['Tuin'], dog['Knuffelbeer'],
                                       dog['Training_sport'], dog['BCDp'], dog['Beschrijving'], dog['Image'])

    def append_dog_data(self, id, name, sex, size, age, dogfriendly, catfriendly, childfriendly, gardenreq, hug, training, BCD, Description, image, score= 0):
        try:

            nieuwe_hond = D.Dog(id, name, size, sex, age, dogfriendly, catfriendly, childfriendly, gardenreq, hug, training, BCD, Description, image)


            self.__recommender_data = self.__recommender_data.append({'dog_id': id, 'name': name, 'size': size, 'sex': sex,
                 'age': age, 'dogfriendly': dogfriendly, 'catfriendly': catfriendly, 'childfriendly': childfriendly,'gardenreq': gardenreq,
                 'hug': hug,'training': training,'BCD': BCD,'score': score,'Description': Description, 'image': image}, ignore_index=True)

            return nieuwe_hond

        except Oepsie as e:
            print(e)


    def add_points(self, id, score):
        df = self.__recommender_data
        for row, dog in df.iterrows():  # .itterrows() geeft een rowindex en data weer in de rij
            if row > 5:
                break
            if dog['dog_id'] == id:
                print("HIT")
                self.__recommender_data.iloc[row, 'score']= score
                print(self.__recommender_data.iloc[row, 'score'])
            else:
                print(dog['dog_id'])
                print("NO-HIT")
                pass



#    .iloc[(self.__recommender_data[dog_id] == dog_id), 'score']



    def give_data(self):
        return self.__recommender_data

    def give_score(self):
        return self.__recommender_data['score']



'''
    def append_data_recommender(self, recommender):
        self.__recommender.append(recommender)  # reservatie toevoegen aan reservatielijst en gegevens reservaties toevoegen aan dataframe
        self.__recommender_data = self.__recommender_data.append(
            {'dog_id': reservatie.geef_reservatie_nummer(), 'name': reservatie.geef_auto().geef_volgnummer_auto(),
             'size': reservatie.geef_starttijd(), 'sex': reservatie.geef_eindtijd(),
             'age': reservatie.geef_beginlocatie(), 'dogfriendly': reservatie.geef_eind_plaats(),
             'catfriendly': reservatie.geef_afstand(), 'childfriendly': reservatie.geef_afstand(),'gardenreq': reservatie.geef_afstand(),
             'hug': reservatie.geef_afstand(),'training': reservatie.geef_afstand(),'BCD': reservatie.geef_afstand(),'score': reservatie.geef_afstand(),}, ignore_index=True)
             
             nieuwe_hond = Dog(id, name, size, sex, age, dogfriendly, catfriendly, childfriendly, gardenreq, hug, training, BCD)
        self.__recommender_data = self.__recommender_data.append({'dog_id': nieuwe_hond.give_id(), 'name': nieuwe_hond.give_name(),
             'size': nieuwe_hond.give_size(), 'sex': nieuwe_hond.give_sex(),
             'age': nieuwe_hond.give_age(), 'dogfriendly': nieuwe_hond.give_dogfriendly(),
             'catfriendly': nieuwe_hond.give_catfriendly(), 'childfriendly': nieuwe_hond.give_childfriendly(),'gardenreq': nieuwe_hond.give_gardenreq(),
             'hug': nieuwe_hond.give_hug(),'training': nieuwe_hond.give_training(),'BCD': nieuwe_hond.give_BCD(),'score': nieuwe_hond.g(),}, ignore_index=True)
        return nieuwe_hond
'''



print('----------')

#probleem: hoe geef je score weer van specifieke hond

groep9 = Databank()
groep9.create_dog()
groep9.add_points(id() , 23) #probleem is dat elke keer een nieuwe ID werd gegenereerd
#print(groep9.give_data())
print(groep9.give_score())
