import pandas as pd

df = pd.read_excel('strona.xlsx')
df.head()
print(df)

df.to_excel('strona.xlsx', sheet_name='dane')

writer = pd.ExcelWriter('strona.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='dane')
df.to_excel(writer, sheet_name='dane', startcol= 3, startrow= 2, index=False)
writer.save()

show = pd.read_excel('strona.xlsx')