class Dog:

    def __init__(self, name, serial, size, sex, age, dogfriendly):
        self.__name = name
        self.__serial = serial
        self.__size = size
        self.__sex = sex
        self.__age = age
        self.__dogfriendly = dogfriendly


    def ToJson(self):
        return {
            name: self.__name,

        }

#output in json