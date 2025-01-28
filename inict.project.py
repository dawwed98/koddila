Zakupy = {"Piekarnia":["chleb", "pączek", "bułki"], "Warzywniaka":["marchew", "seler", "rukola"]}
for sklep, produkty in Zakupy.items():
    print(f"Idę do {sklep.upper()} i kupuję tam {', '.join([produkt.upper() for produkt in produkty])}.")    
print("w sumie kupuje", len(Zakupy["Piekarnia"]) + len(Zakupy["Warzywniaka"]), "produktów")