import pandas as pd
import PyMongo as pm

class Databank:

    def __init__(self):
        self.__recommender_data = pd.DataFrame(
            columns=['dog_id', 'name', 'sex', 'size', 'age', 'dogfriendly', 'petfriendly', 'childfriendly', 'gardenreq',
                     'hug', 'training', 'BCD', 'description', 'image', 'summary', 'link', 'score'])
        self.__filterdata = pd.DataFrame(
            columns=['dog_id', 'name', 'sex', 'size', 'age', 'dogfriendly', 'petfriendly', 'childfriendly', 'gardenreq',
                     'hug', 'training', 'BCD', 'description', 'image', 'summary', 'link', 'score'])
        self.__exp1 = False
        self.__exp2 = False
        self.__exp3 = False
    def create_dog(self):

        df = pd.read_excel("Dogs" + '.xlsx')
        for row, dog in df.iterrows():
            self.append_dog_data(row, dog['Naam'], dog['Geslacht'], dog['Groot'], dog['Leeftijd'], dog['Andere_hond'],
                                 dog['Andere_dieren'], dog['Kinderen'], dog['Tuin'], dog['Knuffelbeer'],
                                 dog['Training_sport'], dog['BCDp'], dog['Beschrijving'], dog['Image'], dog['Summary'],
                                 dog['Link'])

    def append_dog_data(self, id, name, sex, size, age, dogfriendly, petfriendly, childfriendly, gardenreq, hug,
                        training, BCD, Description, image, summary, links, score=0):

        new_row = pd.Series({'dog_id': id, 'name': name, 'size': size, 'sex': sex,
                             'age': age, 'dogfriendly': dogfriendly, 'petfriendly': petfriendly,
                             'childfriendly': childfriendly, 'gardenreq': gardenreq,
                             'hug': hug, 'training': training, 'BCD': BCD, 'score': score, 'description': Description,
                             'image': image, 'summary': summary, 'link': links})
        self.__recommender_data = pd.concat([self.__recommender_data, new_row.to_frame().T], ignore_index=True)

    def add_points(self, id, score):

        for row, dog in self.__recommender_data.iterrows():
            if dog['dog_id'] == id:
                self.__recommender_data.loc[row, 'score'] += score

    def make_recommendation(self, inputdata):
        self.reset_all()
        lijst = []
        for vraagnum, data in inputdata.iterrows():

            input = data['antwoorden']
            gewicht = data['gewichten']

            for row, dog in self.give_data().iterrows():

                # VRAAG 1: Welk geslacht prefereert u?  (eigenschap: geslacht --> reu, teef)
                if vraagnum == 0:
                    if dog['sex'] == input:
                        self.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))

                # VRAAG 2: Welk grootte prefereert u?  (eigenschap: geslacht --> reu, teef)
                if vraagnum == 1:
                    if dog['size'] == input:
                        self.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))

                # VRAAG 3: Leeftijd?  (eigenschap: geslacht --> reu, teef)
                if vraagnum == 2:
                    if dog['age'] == input:
                        self.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))

                # VRAAG 4: Heeft u reeds (een) andere hond(en)? (eigenschap: ja, reu, teef, nee)

                if vraagnum == 3:
                    if dog['dogfriendly'] == input and input == 'Ja, een reu':
                        self.add_points(dog['dog_id'], 2 + ((gewicht - 50) / 50))

                        if dog['dog_id'] in lijst:
                            pass
                        else:
                            lijst.append(dog['dog_id'])

                    if dog['dogfriendly'] == input and input == 'Ja, een teef':
                        self.add_points(dog['dog_id'], 2 + ((gewicht - 50) / 50))

                        if dog['dog_id'] in lijst:
                            pass
                        else:
                            lijst.append(dog['dog_id'])

                    if dog['dogfriendly'] == "Ja, een reu" and input == 'Ja, meerdere honden':
                        self.add_points(dog['dog_id'], 2 + ((gewicht - 50) / 50))

                        if dog['dog_id'] in lijst:
                            pass
                        else:
                            lijst.append(dog['dog_id'])

                    if dog['dogfriendly'] == input and input == 'Nee':

                        if dog['dog_id'] in lijst:
                            pass
                        else:
                            lijst.append(dog['dog_id'])

                # VRAAG 5 want deze vragen hebben dezelfde puntenlogica en 1/1 matching met de dataset
                if vraagnum == 4:
                    if dog['petfriendly'] == input and input == "Ja":
                        self.add_points(dog['dog_id'], 2 + ((gewicht - 50) / 50))

                    if dog['petfriendly'] != input and input == "Ja" and dog['dog_id'] in lijst:
                        lijst.remove(dog['dog_id'])

                # -------- Vanaf hier speciale logica vragen:

                # VRAAG 6: Wat voor gezinssituatie heeft u? (eigenschap: ja, grote, nee)
                if vraagnum == 5:
                    if dog['childfriendly'] == input and input == "Enkel kinderen boven 12 jaar":
                        self.add_points(dog['dog_id'], 2 + ((gewicht - 50) / 50))

                    if dog['childfriendly'] != input and dog['childfriendly'] == "Nee" and dog['dog_id'] in lijst:
                        lijst.remove(dog['dog_id'])

                    else:
                        self.give_all()

                # VRAAG 7: Heeft u een omheinde tuin? (eigenschap: default, moet tuin: ja)
                if vraagnum == 6:
                    if dog['gardenreq'] == input and input == "Nee":
                        self.add_points(dog['dog_id'], 2 + ((gewicht - 50) / 50))

                    if dog['gardenreq'] == input and input == "Ja":
                        self.give_all()

                    if dog['gardenreq'] != input and input == "Nee" and dog['dog_id'] in lijst:
                        lijst.remove(dog['dog_id'])

                # VRAAG 8: Zoekt u een echte knuffelbeer? (eigenschap: default, ja)
                if vraagnum == 7:
                    if dog['hug'] == input and input == "Ja, knuffelkontjes!":  # V8
                        self.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))
                    else:
                        self.give_all()

                # VRAAG 9: Zou u graag training en/of hondensport doen met de hond? (eigenschap: default, training/sport)
                if vraagnum == 8:
                    if dog['training'] == input and input == "Ja, graag!":  # V9
                        self.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))
                    else:
                        self.give_all()

                # VRAAG 10: Prefereert u een hond die getraind wordt via het Belgian Cell Dogs project?* (eigenschap: default, BCDp)
                if vraagnum == 9:
                    if dog['BCD'] == input and input == "Ja":  # V10
                        self.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))
                    else:
                        self.give_all()

        self.addFilterdata(lijst)
        return self.give_top4()

    def give_all(self):
        for row, dog in self.__recommender_data.iterrows():
            self.__recommender_data.loc[row, 'score'] += 1 / len(self.__recommender_data)

    def reset_all(self):
        for row, dog in self.__recommender_data.iterrows():
            self.__recommender_data.loc[row, 'score'] = 0

        self.__filterdata = pd.DataFrame(
            columns=['dog_id', 'name', 'sex', 'size', 'age', 'dogfriendly', 'petfriendly', 'childfriendly', 'gardenreq', 'hug', 'training', 'BCD', 'Description', 'image', 'summary', 'link', 'score'])

    def give_data(self):
        return self.__recommender_data

    def addFilterdata(self, data):
        for item in data:
            for row, dog in self.__recommender_data.iterrows():
                if self.__recommender_data.loc[row, 'dog_id'] == item:
                    self.__filterdata = pd.concat([self.__filterdata, self.__recommender_data.loc[row, :].to_frame().T], ignore_index=True)

    def give_top4(self):

        lijst = []
        double = []

        exp1 = False
        self.__exp1 = False
        exp2 = False
        self.__exp2 = False
        exp3 = False
        self.__exp3 = False

        while len(lijst) < 4:

            if len(self.__filterdata) >= 4:
                for row, data in self.__filterdata.sort_values(by=['score', 'name'], ascending=False).head(4).iterrows():
                    if len(lijst) < 4 and data['name'] not in double:
                        dicti = {}
                        dicti["name"] = data['name']
                        dicti["imgURL"] = data['image']
                        dicti["description"] = data['description']
                        dicti["summary"] = data['summary']
                        dicti["link"] = data['link']
                        double.append(data['name'])
                        lijst.append(dicti)

                if len(lijst) >= 4:
                    exp1 = True

            if len(self.__filterdata) > 0 and len(self.__filterdata) < 4:
                for row, data in self.__filterdata.sort_values(by=['score', 'name'], ascending=False).head(4).iterrows():
                    if len(lijst) < 4 and data['name'] not in double:
                        dicti = {}
                        dicti["name"] = data['name']
                        dicti["imgURL"] = data['image']
                        dicti["description"] = data['description']
                        dicti["summary"] = data['summary']
                        dicti["link"] = data['link']
                        double.append(data['name'])
                        lijst.append(dicti)

                for row, data in self.__recommender_data.sort_values(by=['score', 'name'], ascending=False).head(4).iterrows():
                    if len(lijst) < 4 and data['name'] not in double:
                        dicti = {}
                        dicti["name"] = data['name']
                        dicti["imgURL"] = data['image']
                        dicti["description"] = data['description']
                        dicti["summary"] = data['summary']
                        dicti["link"] = data['link']
                        lijst.append(dicti)

                if len(lijst) >= 4:
                    exp2 = True

            if len(self.__filterdata) == 0:
                for row, data in self.__recommender_data.sort_values(by=['score', 'name'], ascending=False).head(4).iterrows():
                    if len(lijst) < 4 and data['name'] not in double:
                        dicti = {}
                        dicti["name"] = data['name']
                        dicti["imgURL"] = data['image']
                        dicti["description"] = data['description']
                        dicti["summary"] = data['summary']
                        dicti["link"] = data['link']
                        lijst.append(dicti)

                if len(lijst) >= 4:
                    exp3 = True


        if exp1:
            self.__exp1 = True
        if exp2:
            self.__exp2 = True
        if exp3:
            self.__exp3 = True

        return lijst

    def export_mongo(self, lijst):

        #identificatie = id(lijst)
        data = lijst
        ExceptionHandling = ""

        if self.__exp1:
            ExceptionHandling = "VOLLEDIG"
        if self.__exp2:
            ExceptionHandling = "DEELS"
        if self.__exp3:
            ExceptionHandling = "NIET"

        data.append({"exception": ExceptionHandling})

        x= pm.get_database()
        y= pm.insertData(data, x)
        pm.exitdb()

        return y

    def read_mongo(self, id):

        x = pm.get_database()
        data = pm.getData(id, x)
        pm.exitdb()

        return data

    def find_and_export(self, id, lijst):

        x = pm.get_database()
        feedback = pm.addResearch(id, lijst, x)
        pm.exitdb()

        return feedback

