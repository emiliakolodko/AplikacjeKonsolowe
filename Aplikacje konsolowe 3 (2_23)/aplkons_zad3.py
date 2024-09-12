class Notatka:
    __licznikNotatek = 0
    def __init__(self, tytul, tresc):
        Notatka.__licznikNotatek += 1

        self.__id = Notatka.__licznikNotatek
        self.__tytul = tytul
        self.__tresc = tresc

    def wyswietlNotatke(self):
        return f"Tytuł: {self.__tytul}\nTreść: {self.__tresc}"

    def pokazDiagnostyke(self):
        return f"{self.__id};{self.__tytul};{self.__tresc}"

if __name__ == "__main__":
    notatka1 = Notatka("Zakupy", "Karotka, Sok pomarańczowy, 2kg kurczaka")
    notatka2 = Notatka("Kalendarze", "Impreza 14 wrzesnia, Fizjo 13 wrzesnia pzdr")
    print(notatka1.wyswietlNotatke(), "\n")
    print(notatka2.wyswietlNotatke(), "\n")
    print(notatka1.pokazDiagnostyke())
    print(notatka2.pokazDiagnostyke())