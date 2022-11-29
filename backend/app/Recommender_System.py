
import pandas as pd
from openpyxl import load_workbook


class Databank:

    def __init__(self):
        self.__recommender_data = pd.DataFrame(columns=['dog_id', 'name', 'sex', 'size', 'age', 'dogfriendly', 'petfriendly','childfriendly','gardenreq','hug','training','BCD','Description','image','summary','link','label','score'])  # dataframe maken; handig voor doorzoeken
        self.__filterdata = pd.DataFrame(columns=['dog_id', 'name', 'sex', 'size', 'age', 'dogfriendly', 'petfriendly','childfriendly','gardenreq','hug','training','BCD','Description','image','summary','link','score'])

    def create_dog(self):

        df = pd.read_excel("Dogs" + '.xlsx')  # data inlezen
        for row, dog in df.iterrows():  # .itterrows() geeft een rowindex en data weer in de rij
            self.append_dog_data(row, dog['Naam'], dog['Geslacht'], dog['Groot'], dog['Leeftijd'], dog['Andere_hond'], dog['Andere_dieren'], dog['Kinderen'], dog['Tuin'], dog['Knuffelbeer'], dog['Training_sport'], dog['BCDp'], dog['Beschrijving'], dog['Image'], dog['Summary'], dog['Links'])

    def append_dog_data(self, id, name, sex, size, age, dogfriendly, petfriendly, childfriendly, gardenreq, hug, training, BCD, Description, image, summary, label= '',links,score= 0):

        new_row = pd.Series({'dog_id': id, 'name': name, 'size': size, 'sex': sex,
             'age': age, 'dogfriendly': dogfriendly, 'petfriendly': petfriendly, 'childfriendly': childfriendly,'gardenreq': gardenreq,
             'hug': hug,'training': training,'BCD': BCD,'score': score,'description': Description, 'image': image, 'summary': summary,'link': links, 'label':label})
        self.__recommender_data = pd.concat([self.__recommender_data, new_row.to_frame().T], ignore_index=True) #aangezien een pd.series 1 kolom geeft met de vragen als rij moeten we transponern met .T

    def add_points(self, id, score):
        for row, dog in self.__recommender_data.iterrows():  # .itterrows() geeft een rowindex en data weer in de rij
            if dog['dog_id'] == id:
                self.__recommender_data.loc[row, 'score']+= score



    def make_recommendation(self, inputdata):
        for vraagnum, data in inputdata.iterrows():


            input = data['antwoorden']
            gewicht = data['gewichten']
            dog_list = []

            for row, dog in self.give_data().iterrows():  # we gaan door elke hond in onze database

                # VRAAG 1: Welk geslacht prefereert u?  (eigenschap: geslacht → reu, teef)
                if vraagnum == 0: #Merk op dat de indices begint bij 0 en NIET 1
                    if dog['sex'] == input:  # V1: We willen absoluut de juiste geslacht honden, daarom 2 als basis
                        self.add_points(dog['dog_id'], 3 + ((gewicht - 50) / 50))

                # VRAAG 2: Welk grootte prefereert u?  (eigenschap: geslacht → reu, teef)
                if vraagnum == 1:
                    if dog['size'] == input:  # V2: We willen ook zeker de juiste grootte, maar minder belangrijk dan geslacht
                        self.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))

                # VRAAG 3: Leeftijd?  (eigenschap: geslacht → reu, teef)
                if vraagnum == 2:
                    if dog['age'] == input:  # V2: We willen ook zeker de juiste grootte, maar minder belangrijk dan geslacht
                        self.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))

                #VRAAG 4: Heeft u reeds (een) andere hond(en)? (eigenschap: ja, reu, teef, nee)
                #Note to self: te harde codering!
                if vraagnum == 3:
                    if dog['dogfriendly'] == input and input == 'Ja, een reu':
                        self.add_points(dog['dog_id'], 2.5 + ((gewicht - 50) / 50))

                    if dog['dogfriendly'] == input and input == 'Ja, een teef':
                        self.add_points(dog['dog_id'], 2.5 + ((gewicht - 50) / 50))

                    if dog['dogfriendly'] == input and input == 'Ja, meerdere honden':
                        self.add_points(dog['dog_id'], 2.5 + ((gewicht - 50) / 50))

                    if dog['dogfriendly'] == input and input == 'Nee':
                        self.add_points(dog['dog_id'], 2.5 + ((gewicht - 50) / 50))

                # VRAAG 5 want deze vragen hebben dezelfde puntenlogica en 1/1 matching met de dataset
                if vraagnum == 4:
                    if dog['petfriendly'] == input:  # V3: Gewicht beslissen mensen zelf
                        self.add_points(dog['dog_id'], 2.5 + ((gewicht - 50) / 50))

#-------- Vanaf hier speciale logica vragen:
                # Note to self: te harde codering!
                # VRAAG 6: Wat voor gezinssituatie heeft u? (eigenschap: ja, grote, nee)
                if vraagnum == 5:
                    if dog['childfriendly'] == input and input == "Enkel kinderen boven 12 jaar":
                        self.add_points(dog['dog_id'], 2.5 + ((gewicht - 50) / 50))

                    else:  # V6 als er dus enkel volwassene zijn krijgt iedereen een punt
                        self.give_all()

                # --------
                # VRAAG 7: Heeft u een omheinde tuin? (eigenschap: default, moet tuin: ja)
                if vraagnum == 6:
                    if dog['gardenreq'] == input and input == "Nee":  # V7, indien input "nee" dan enkel honden met
                        self.add_points(dog['dog_id'], 2.5 + ((gewicht - 50) / 50))

                    if dog['gardenreq'] == input and input == "Ja":  # V7, indien input "ja" dan alle honden een punt, equivalent als zeggen dat niemand iets krijgt.
                        self.give_all()

                # --------
                # VRAAG 8: Zoekt u een echte knuffelbeer? (eigenschap: default, ja)
                if vraagnum == 7:
                    if dog['hug'] == input and input == "Ja, knuffelkontjes!":  # V8
                        self.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))
                    else:
                        self.give_all()

                # --------
                # VRAAG 9: Zou u graag training en/of hondensport doen met de hond? (eigenschap: default, training/sport)
                if vraagnum == 8:
                    if dog['training'] == input and input == "Ja, graag!":  # V9
                        self.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))
                    else:
                         self.give_all()

                # --------
                #VRAAG 10: Prefereert u een hond die getraind wordt via het Belgian Cell Dogs project?* (eigenschap: default, BCDp)
                if vraagnum == 9:
                    if dog['BCD'] == input and input == "Ja":  # V10
                        self.add_points(dog['dog_id'], 1 + ((gewicht - 50) / 50))
                    else:
                         self.give_all()

        return self.give_top4()

    def give_all(self):
        for row, dog in self.__recommender_data.iterrows():  # .itterrows() geeft een rowindex en data weer in de row
            self.__recommender_data.loc[row, 'score']+= 1/len(self.__recommender_data) #we normalizeren tegenover het aantal honden in de lijst

    def give_data(self):
        return self.__recommender_data

    def search_dupl(self):
        for row1, dog1 in self.__recommender_data.iterrows():  # .itterrows() geeft een rowindex en data weer in de rij
            count =1
            for row2, dog2 in self.__recommender_data.iterrows():
                if row1==row2:
                    break
                else:
                    if dog1['name']== dog2['name']:
                        self.__recommender_data.loc[row1, 'score'] = self.__recommender_data.loc[row2, 'score']

    def give_top4(self):

        self.search_dupl() #om honden die samengezet moeten worden dezelfde punten gaan krijgen, assumptie: enkel duplicates in data indien ze samen horen
        for row, data in self.__recommender_data.iterrows():
            x = self.__recommender_data.loc[row, 'score']
            self.__recommender_data.loc[row, 'score'] = round(x, 3) #want 10 is de schaal waarmee we werken

        lijst = []
        for row, data in self.__recommender_data.sort_values(by=['score', 'name'], ascending=False).head(4).iterrows():
            dicti = {}
            dicti["name"] = data['name']
            dicti["imgURL"] = data['image']
            dicti["description"] = data['description']
            dicti["summary"] = data['summary']
            dicti["link"] = data['link']
            lijst.append(dicti)
        return lijst

    def export_excel(self, lijst):
        workbook = load_workbook('./records.xlsx')  # je laadt een workbook
        ws = workbook.active  # je activeert e workbook
        identificatie= id(lijst) #elke run zal er een andere id gegeneert worden obv van dit getal
        inzet = [identificatie] #meer leren of IDENT ID
        for dicts in lijst:
            for key, value in dicts.items():
                inzet.append(value)

        ws.append(inzet)
        workbook.template = False
        workbook.save('./records.xlsx')
        return identificatie

    def read_excel(self, id):
        workbook = load_workbook('./records.xlsx')  # je laadt een workbook
        ws = workbook.active  # je activeert e workbook
        lijst=[]
        for row in ws.iter_rows(min_row=2, max_col= 21):
            if row[0].value == id: #Dus de rij met het specifieke ID maar de id moet niet terug meegegeven worden
                for x in range(0,16):
                    if x==0 or x==5 or x==10 or x==15:

                        dicti={}
                        dicti["name"] = row[1+x].value
                        dicti["imgURL"] = row[2+x].value
                        dicti["description"] = row[3+x].value
                        dicti["summary"] = row[4+x].value
                        dicti["link"] = row[5+x].value
                        lijst.append(dicti)
                        lijst
        return lijst

    def find_and_export(self, id, lijst):
        workbook = load_workbook('./records.xlsx')  # je laadt een workbook
        ws = workbook.active  # je activeert e workbook
        for index in ws.iter_rows(min_row=2):
            if index[0].value == id: #Dus de rij met het specifieke ID maar de id moet niet terug meegegeven worden

                for column in ["Y", "Z", "AA", "AB"]:  # Here you can add or reduce the columns
                    if column == "Y":
                        cell_name = "{}{}".format(column, index[0].row)
                        ws[cell_name].value  = lijst[0]# the value of the specific cell
                    if column == "Z":
                        cell_name = "{}{}".format(column, index[0].row)
                        ws[cell_name].value = lijst[1]  # the value of the specific cell
                    if column == "AA":
                        cell_name = "{}{}".format(column, index[0].row)
                        ws[cell_name].value = lijst[2]  # the value of the specific cell
                    if column == "AB":
                        cell_name = "{}{}".format(column, index[0].row)
                        ws[cell_name].value = lijst[3]  # the value of the specific cell

        workbook.save('./records.xlsx')



Sys = Databank()
Sys.create_dog()

#OPM: dit is een test input en volledig fictief / Voor de meeste input zullen een paar honden dezelfde scores hebben, dit is normaal aangezien de dataset beperkt is en dus niet elke hond uniek
antwoorden = ['Reu', 'Eerder groot', 'Gouden senioren jaren (2014 en ouder)', 'Nee', 'Nee', 'Nee', 'Ja', 'Ja, knuffelkontjes!', 'Dat is voor mij niet zo belangrijk', 'Nee'] #Met deze antwoorden vind je Max en Sky
gewichten = [100, 50, 50, 50, 50, 100, 10, 80, 100, 50] #je kan spelen met de gewichten, 50 wilt zeggen neutraal.
#antwoorden
#gewichten = []
d= {'antwoorden': antwoorden, 'gewichten': gewichten}
inputdata = pd.DataFrame(d)


x= Sys.make_recommendation(inputdata)
print(x)


