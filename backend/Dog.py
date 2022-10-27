class Dog:

    def __init__(self, id, name, size, sex, age, dogfriendly, catfriendly, childfriendly, gardenreq, hug, training, BCD):
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



    def ToJson(self):
        return {
            name: self.__name,

        }

#output in jsonss