import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(message)s', filename='zad 4.4.log')
logging.debug('Start of program')
liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
typ_obluczenia = int(input("Podaj typ obliczenia (1-dodawanie, 2-odejmowanie, 3-mnożenie, 4-dzielenie): "))
if typ_obluczenia == 1:
    logging.info(f"Dodawanie liczb {liczba1} i {liczba2}")
    wynik = liczba1 + liczba2
elif typ_obluczenia == 2:
    logging.info(f"Odejmowanie liczb {liczba1} i {liczba2}")
    wynik = liczba1 - liczba2
elif typ_obluczenia == 3:
    logging.info(f"Mnożenie liczb {liczba1} i {liczba2}")
    wynik = liczba1 * liczba2
elif typ_obluczenia == 4:
    logging.info(f"Dzielenie liczb {liczba1} i {liczba2}")
    wynik = liczba1 / liczba2
else:
    logging.error("Nieprawidłowy wybór")
    wynik = "Błąd"

if wynik != "Błąd":
    print(f"Wynik: {wynik}")
    logging.debug(f"Wynik obliczeń: {wynik}")