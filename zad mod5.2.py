import random

class Film:
    def __init__(self, tytuł, rok_wydania, gatunek, liczba_odtworzeń=0):
        self.tytuł = tytuł
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzeń = liczba_odtworzeń
    
    def play(self):
        self.liczba_odtworzeń += 1
        return self.liczba_odtworzeń
    
    def __str__(self):
        return f"{self.tytuł} ({self.rok_wydania})"

class Seriale(Film):
    def __init__(self, tytuł, rok_wydania, gatunek, numer_sezonu, numer_odcinka, liczba_odtworzeń=0):
        super().__init__(tytuł, rok_wydania, gatunek, liczba_odtworzeń)
        self.numer_sezonu = numer_sezonu
        self.numer_odcinka = numer_odcinka
   
    def __str__(self):
        return f"{self.tytuł} S{self.numer_sezonu}E{self.numer_odcinka}"

# Lista filmów i seriali
filmy_i_seriale = [
    Film("Pulp Fiction", 1994, "crime"),
    Film("Matrix", 1999, "sci-fi"),
    Seriale("The Simpsons", 1989, "animation", 1, 1),
    Seriale("Friends", 1994, "comedy", 1, 5)
]

def get_movies():
    filmy = [element for element in filmy_i_seriale if isinstance(element, Film)]
    filmy.sort(key=lambda x: x.tytuł)
    return filmy

def get_series():
    seriale = [element for element in filmy_i_seriale if isinstance(element, Seriale)]
    seriale.sort(key=lambda x: x.tytuł)
    return seriale

def search(title):
    for element in filmy_i_seriale:
        if title == element.tytuł:
            return element
    return None

def genarate_views():
    element = random.choice(filmy_i_seriale)
    liczba = random.randint(1, 100)
    element.liczba_odtworzeń += liczba

def generate_views():
    for _ in range(10):
        genarate_views()

def top_titles(content_type, n):
    if content_type == "filmy":
        filmy = get_movies()
        filmy.sort(key=lambda x: x.liczba_odtworzeń, reverse=True)
        return filmy[:n]
    elif content_type == "seriale":
        seriale = get_series()
        seriale.sort(key=lambda x: x.liczba_odtworzeń, reverse=True)
        return seriale[:n]
    else:
        return filmy_i_seriale
    
top_titles("filmy", 1)


# Odtwarzanie filmów i seriali
filmy_i_seriale[0].play()

for element in filmy_i_seriale:
    print(element)
    print(element.play())