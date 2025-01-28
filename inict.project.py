Piekarnia = ["chleb", "pączek", "bułki"]
Warzywniak = ["marchew", "seler", "rukola"]
Sklepy = ["Piekarnia", "Warzywniak"]
Piekarnia = [iteam.title() for iteam in Piekarnia]
Warzywniak = [iteam.title() for iteam in Warzywniak]
print("Lista zakupów:")
print("Ide do", Sklepy[0], "i kupuję tam następujące rzeczy:", (Piekarnia))
print("Ide do", Sklepy[1], "i kupuję tam następujące rzeczy:", (Warzywniak))
print("w sumie kupuje", len(Piekarnia) + len(Warzywniak), "produktów")