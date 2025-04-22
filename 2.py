import matplotlib.pyplot as plt
import pandas as pd

# Example data for zliczenia
data = {'Dzień tygodnia': ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek'],
		'Liczba interwencji': [5, 7, 6, 8, 4]}
zliczenia = pd.DataFrame(data).set_index('Dzień tygodnia')

zliczenia.plot(kind='bar', color='skyblue')
plt.title('Zliczenie interwencji według dnia tygodnia')
plt.xlabel('Dzień tygodnia')
plt.ylabel('Liczba interwencji')
plt.xticks(rotation=45)
plt.grid(axis='y')
