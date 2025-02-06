class Wizytówka:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email
    def contact(self):
        print(f"Kontaktuj się z {self.imie} {self.nazwisko}:\n- telefonicznie: {self.telefon}\n- mailowo: {self.email}")
    @property
    def label_length(self):
        return len(self.imie) + len(self.nazwisko)
wizytówka_dawid = Wizytówka("Dawid", "Wędrowski", "123456789", "daw@google.com")
wizytówka_dawid.contact()
print(wizytówka_dawid)    