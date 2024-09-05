class Film:
    def __init__(self, tytul = "", liczbaWypozyczen = 0):
        self._tytul = tytul
        self._liczbaWypozyczen = liczbaWypozyczen

    def get_tytul(self):
        return f"Tytuł: {self._tytul}"

    def set_tytul(self, value):
        self._tytul = value

    def get_liczbaWypozyczen(self):
        return f"Liczba wypożyczeń: {self._liczbaWypozyczen}"

    def dodaj_liczbaWypozyczen(self):
        self._liczbaWypozyczen += 1

    def __str__(self):
        return f"Tytuł: {self._tytul}\nLiczba wypożyczeń: {self._liczbaWypozyczen}"

#Stworz obiekt -> Wyswietl pola obiektu
Obiekt = Film("Jakis Tytuł")

print(Obiekt)

#Zmien tytul obiektu -> Spradz zmieniony tytul obiektu
Obiekt.set_tytul("Inny Tytuł")

print(Obiekt.get_tytul())

#Sprawdz ilosc wypozyczen -> Test inkrementacji ilosci wypozyczen -> Sprawdz ilosc wypozyczen
print(Obiekt.get_liczbaWypozyczen())

Obiekt.dodaj_liczbaWypozyczen()

print(Obiekt.get_liczbaWypozyczen())
