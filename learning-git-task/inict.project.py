Zakupy = {"Piekarnia":["chleb", "pączek", "bułki"], "Warzywniaka":["marchew", "seler", "rukola"]}
print("Lista zakupów:")
print("Piekarnia:", ", ".join(Zakupy["Piekarnia"]))
print("Warzywniak:", ", ".join(Zakupy["Warzywniaka"]))
print("w sumie kupuje", len(Zakupy["Piekarnia"]) + len(Zakupy["Warzywniaka"]), "produktów")