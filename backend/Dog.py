class Dog:

    def __init__(self, id, name, sex, size, age, dogfriendly=True, catfriendly=True, childfriendly=True, gardenreq=True,
                 hug=True, training=True, BCD=False, score=0):

        ### dogfriendly, catfriendly, childfriendly, gardenreq, hug, training en BCD moeten worden aangepast zoals in volgend voorbeeld indien anders dan de defaultwaarde:
        ### Billie = Dier(1, 'Billie', 'teef','klein', 2, dogfriendly=  False, training= False)
        ### defaultwaardes moeten altijd op het einde van de init staan

        self.__id = id
        self.__name = name
        self.__size = size
        self.__sex = sex
        self.__age = age
        self.__dogfriendly = dogfriendly
        self.__catfriendly = catfriendly
        self.__childfriendly = childfriendly
        self.__gardenreq = gardenreq
        self.__hug = hug
        self.__training = training
        self.__BCD = BCD
        self.__score = score



    def give_records(self):
        return print("Het dier noemt" + " " + self.give_name() + " en heeft volgnummer " + str(self.give_id()) + ". \n" +self.give_name() + " is een " + self.give_sex() + " met " + self.give_size() + " gestalte. \n" + self.give_dogfriendly() + "\n"+ self.give_catfriendly()+ "\n"+ self.give_childfriendly() +"\n" + self.give_gardenreq() +"\n"+ self.give_hug() +"\n"+ self.give_training() +"\n"+ self.give_BCD())
    def give_id(self):
        return self.__id

    def give_name(self):
        return self.__name

    def give_sex(self):
        return self.__sex

    def give_size(self):
        return self.__size

    def give_dogfriendly_bool(self):
        return self.__dogfriendly

    def give_dogfriendly(self):
        if self.__dogfriendly == True:
            return "Deze hond kan goed met andere honden om. "
        elif self.__dogfriendly == False:
            return "Deze hond is niet hondvriendelijk. "

    def give_catfriendly_bool(self):
        return self.__catfriendly

    def give_catfriendly(self):
        if self.__catfriendly == True:
            return 'Deze hond is wel katvriendelijk. '
        elif self.__catfriendly == False:
            return 'Deze hond is niet katvriendelijk. '
    def give_childfriendly_bool(self):
        return self.__childfriendly

    def give_childfriendly(self):
        if self.__childfriendly == True:
            return 'De hond is wel kindvriendelijk. '
        elif self.__childfriendly == False:
            return 'De hond is niet kindvriendelijk. '
    def give_gardenreq_bool(self):
        return self.__gardenreq

    def give_gardenreq(self):
        if self.__gardenreq == True:
            return 'Voor deze hond is een tuin noodzakelijk. '
        else:
            return 'Voor deze hond is een tuin niet noodzakelijk maar wel aangeraden. '


    def give_hug_bool(self):
        return self.__hug

    def give_hug(self):
        if self.__hug == True:
            return 'De hond is een echte knuffelbeer. '
        elif self.__hug == False:
            return 'De hond is niet de grootste knuffelbeer. '
    def give_training_bool(self):
        return self.__training

    def give_training(self):
        if self.__training ==True:
            return 'Training met deze hond is mogelijk. '
        else:
            return 'Deze hond is niet geschikt voor intensieve trainingen. '
    def give_BCD_bool(self):
        return self.__BCD

    def give_BCD(self):
        if self.__BCD == True:
            return 'De hond is getraind door het BCD programma. '
        else:
            return 'De hond heeft geen BCD trainingsprogramma gevolgd. '

    def give_score(self):
        return self.__score

    def higher_score(self, value): #telkens wanneer de eigenschap van de hond voldoet aan het antwoord van de gebruiker,stijgt de score van de hond voor deze gebruiker
        self.__score = self.__score + value


    def assign_id(self, newid):
        self.__id = newid


Billie = Dog(1, 'Billie', 'teef', 'klein', 2, dogfriendly = True, training = False)
Billie.assign_id(20)
#Silver = Dog(2, )


Billie.give_catfriendly()
print(Billie.give_score())
Billie.higher_score(5)
print(Billie.give_score())
Billie.give_records()



   # def ToJson(self):
       # return {
          #  name: self.__name,

        #}"""

#output in jsonss


