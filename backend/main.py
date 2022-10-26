

class Dier:

    def __init__(self, naam, volgnummer, type, kleur, gedrag, actief= False):
        self.__naamin = naam
        self.__volgnummerin = volgnummer
        self.__typein = type #type slaat op wat voor dier dit is
        self.__kleurin = kleur
        self.__gedragin = gedrag
        self.__actiefin = actief #of het dier veel moet bewegen


    def geefgegevens(self):

        return "Het dier noemt" + " " + self.__naamin + " en heeft volgnummer " + str(self.__volgnummerin)





Charlotte = Dier("Charlotte :)", 7, "mens", "blond", "aardig", True)

print(Charlotte.geefgegevens())
print("hello world")