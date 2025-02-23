class Film:
    def __init__(self, tytuł, rok_wydania, gatunek, liczba_odtworzeń):
        self.tytuł = tytuł
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzeń = liczba_odtworzeń
    def play(self):
        self.liczba_odtworzeń += 1
        return self.liczba_odtworzeń
    

    def __str__(self):
        return f"{self.tytuł} ({self.rok_wydania})"

    def play(self):
        self.liczba_odtworzeń += 1
        return self.liczba_odtworzeń

class Seriale(Film):
    def __init__(self, tytuł, rok_wydania, gatunek, liczba_odtworzeń, numer_sezonu, numer_odcinka):
        super().__init__(tytuł, rok_wydania, gatunek, liczba_odtworzeń)
        self.numer_sezonu = numer_sezonu
        self.numer_odcinka = numer_odcinka
    def __str__(self):
        return f"{self.tytuł} S{self.numer_sezonu}E{self.numer_odcinka}"

    def play(self):
        self.liczba_odtworzeń += 1
        return self.liczba_odtworzeń
# Lista filmów i seriali
filmy_i_seriale = [
    Film("Pulp Fiction", 1994, "crime", 0),
    Film("Matrix", 1999, "sci-fi", 0),
    Seriale("The Simpsons", 1989, "animation", 0, 1, 1),
    Seriale("Friends", 1994, "comedy", 0, 1, 5)
]

# Odtwarzanie filmów i seriali
filmy_i_seriale[0].play()

for element in filmy_i_seriale:
    print(element)
    print(element.play())