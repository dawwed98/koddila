from faker import Faker
import random

fake = Faker()
class Film:
    counter = 0
    film_list = [
       
    ]
    
    def __init__(self, tytuł, rok_wydania, gatunek, liczba_odtworzeń):
        self.tytuł = tytuł
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzeń = liczba_odtworzeń
        Film.counter += 1
        Film.film_list.append(self)

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

for i in range(5):
    film = Film(tytuł=fake.catch_phrase(), rok_wydania=random.randint(1900, 2021), gatunek=fake.word(), liczba_odtworzeń=random.randint(0, 100))
    print(film)
    print(film.play())
for i in range(5):  
    film = Seriale(tytuł=fake.catch_phrase(), rok_wydania=random.randint(1900, 2021), gatunek=fake.word(), liczba_odtworzeń=random.randint(0, 100), numer_sezonu=random.randint(1, 10), numer_odcinka=random.randint(1, 20))
    print(film)
    print(film.play())
print(Film.counter)