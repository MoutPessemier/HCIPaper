class Dog:

    def __init__(self, name, volgnummer, grootte, geslacht, leeftijd, hondvriendelijk):
        self.__name = name
        self.__volgnummerin = volgnummer
        self.__groottein = grootte
        self.__leeftijdin = leeftijd
        self.__hondvriendelijkin = hondvriendelijk


    def ToJson(self):
        return {
            name: self.__name,

        }

#output in jsonss