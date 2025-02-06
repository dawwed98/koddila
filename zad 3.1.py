#zad 3.1
Zakupy = {"Piekarnia":["chleb", "pączek", "bułki"], "Warzywniaka":["marchew", "seler", "rukola"]}

Zakupy["Piekarnia"].append("ciastko")

for sklep, produkty in Zakupy.items():
    print(f"Idę do {sklep.upper()} i kupuję tam {', '.join([produkt.upper() for produkt in produkty])}.")    

print("w sumie kupuje", len(Zakupy["Piekarnia"]) + len(Zakupy["Warzywniaka"]), "produktów")

#zad 3.2
for i in range(101):
    if i % 5 == 0:
        print(f"{i} jest podzielne przez 5")
for i in range(101):
    if i % 3 == 0:
        print({i**3}, end = " ")