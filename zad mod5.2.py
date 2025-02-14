class Film:
    def __init__(self, tytuł, rok_wydania, gatunek, liczba_odtworzeń):
        self.tytuł = tytuł
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzeń = liczba_odtworzeń
    def __str__(self):
        return f"{self.tytuł} ({self.rok_wydania})"

class Seriale(Film):
    def __init__(self, tytuł, rok_wydania, gatunek, liczba_odtworzeń, numer_sezonu, numer_odcinka):
        super().__init__(tytuł, rok_wydania, gatunek, liczba_odtworzeń)
        self.numer_sezonu = numer_sezonu
        self.numer_odcinka = numer_odcinka
    def __str__(self):
        return f"{self.tytuł} S{self.numer_sezonu}E{self.numer_odcinka}"

object1 = Film("Wiedźmin", 2019, "Fantasy", 100)
object2 = Seriale("Wiedźmin", 2019, "Fantasy", 100, 1, 1)
print(object1)
print(object2)
