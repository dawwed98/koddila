import pandas as pd

df = pd.read_excel('a3.xlsx')

df.rename(columns={'Unnamed: 0': 'Lp.', 'Unnamed: 1': 'Pozycja', 'Unnamed: 2': 'Tytuł', 'ARTIST': 'Autor', 'Unnamed: 4': 'Data wydania', 'HIGH POSN': 'Max pozycja'}, inplace=True)
df.head()
print(df)
                   
writer = pd.ExcelWriter('a3.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='dane')
df.to_excel(writer, sheet_name='dane', startcol= 0, startrow= 1, index=False)
writer.close()
show = pd.read_excel('a3.xlsx')
print(show)