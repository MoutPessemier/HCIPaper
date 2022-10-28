#if you are commits behind master: checkout on branch, then pull into current merge from master origin (remote)

import datetime as dt
import pandas as pd
import numpy as py
import pandas as pd
import Dog as D



class Recommender:

    def __init__(self):
        self.__recommender = []  # lijst van reservaties maken; handig bij opvragen van gegevens
        self.__recommender_data = pd.DataFrame(columns=['dog_id', 'name', 'size', 'sex', 'age', 'dogfriendly', 'catfriendly','childfriendly','gardenreq','hug','training','BCD','score'])  # dataframe maken; handig voor doorzoeken

    def append_dog_data(self, id, name, size, sex, age, dogfriendly, catfriendly, childfriendly, gardenreq, hug, training, BCD, score= 0):
        try:
            nieuwe_hond = D.Dog(id, name, size, sex, age, dogfriendly, catfriendly, childfriendly, gardenreq, hug, training, BCD)
            self.__recommender_data = self.__recommender_data.append({'dog_id': id, 'name': name, 'size': size, 'sex': sex,
                 'age': age, 'dogfriendly': dogfriendly, 'catfriendly': catfriendly, 'childfriendly': childfriendly,'gardenreq': gardenreq,
                 'hug': hug,'training': training,'BCD': BCD,'score': score,}, ignore_index=True)

            return nieuwe_hond

        except Oepsie as e:
            print(e)


    def give_data(self):
        return self.__recommender_data


groep9= Recommender()

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



#---------------------------------------------------
#Exeption handling

class Oepsie(Exception):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'There was a problem reading the data'

class OutputGivenInput(Exception):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'Attention, output given as input'

#---------------------------------------------------
# Inlezen data, is enkel leuk voor testing, nog aan te passen later:

bool = False

while not bool:

    #print('\n')
    #value = input("Geef uw bestandsnaam in, gevolgd door enter (ZONDER '.csv' extensie): ")

    try:

        df = pd.read_csv("DogdataTest" + '.csv', nrows=10000)
        bool = True
        print('\n')
        print('File loaded')
        print('\n')

    except OutputGivenInput as o:
        print(o)

    except FileNotFoundError:

        print('---------------------------------')
        print('Attention, did you add ".csv"? You need to leave ".csv". Otherwise check the name of your file.')
        print('Please try again:')
        print('---------------------------------')


#Nu gaan we de dataobject hond aanmaken en al direct in onze recommender systeem steken
for row, dog in df.iterrows(): #.itterrows() geeft een rowindex en data weer in de rij
    if row > len(df):
        break

    else:
        # print('\nRow number:', row)
        # print('Row-data:\n', dog)
        # print('The value of \'name\' in this row:', dog['name'])
        groep9.append_dog_data(dog['id'], dog['name'], dog['size'], dog['sex'], dog['age'], dog['dogfriendly'], dog['catfriendly'], dog['childfriendly'], dog['gardenreq'], dog['hug'], dog['training'], dog['BCD'])


print(groep9.give_data()['name'])

#---------------------------------------------------
#Hier testen we alles
#print(df.info())
# print(df.iloc[1, 0:8]) #voor rij 1 in de dataset print dan kolommen 0 tot 7
# print('\n') #een witregel
# print(df["name"]) #print de kolom name voor alle rijen
# print('\n') #een witregel






Billie = D.Dog(1, 'Billie', 'teef', 'klein', 2, dogfriendly = True, training = False) #eerst moet je "D." gebruiken om de andere .py file op te roepen. Dan kan je alle functies gebruiken
Billie.assign_id(20)
#Silver = Dog(2, )Billie.give_catfriendly()
#print(Billie.give_score())
Billie.higher_score(5)
#print(Billie.give_score())
#Billie.give_records()
