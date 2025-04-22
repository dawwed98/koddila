import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Example dataset for demonstration
data = {'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 
				'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']}
df = pd.DataFrame(data)

df['day'].value_counts().plot(kind='bar', color='skyblue', title='Zliczenie interwencji według dnia tygodnia')
plt.xlabel('Day of the Week')
plt.ylabel('Counts')
plt.show()