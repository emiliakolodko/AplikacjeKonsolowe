class Osoba:
    classInstances = 0
    def __init__(self, id = 0, imie = ""):
        Osoba.classInstances += 1

        self.__id = id
        self.__imie = imie

    def copyObject(self, obj):
        return Osoba(obj.__id, obj.__imie)

osoba1 = Osoba(1, "Janek")
osoba2 = osoba1.copyObject(osoba1)
print(osoba1, osoba2)
print(Osoba.classInstances)
