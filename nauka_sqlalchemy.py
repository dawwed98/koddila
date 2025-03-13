import sqlalchemy
import csv

csv_file = 'clean_stations (1).csv'
csv_file2 = 'clean_measure (1).csv'
db_name = 'zadanie.db'

conn = sqlalchemy.connect(db_name)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS stations (
    station text PRIMARY KEY,
    latitude real,
    longitude real,
    elevation real,
    name text,
    country text,
    state text
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS measurements (
    station text,
    date DATE PRIMARY KEY,
    precip real,
    tobs real
);
''')

with open(csv_file, 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            latitude = float(row['latitude'])
            longitude = float(row['longitude'])
            elevation = float(row['elevation'])
            cursor.execute('''
            INSERT OR IGNORE INTO stations (station, latitude, longitude, elevation, name, country, state)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (row['station'], latitude, longitude, elevation, row['name'], row['country'], row['state']))
        except ValueError as e:
            print(f"Error in stations table: {e} for row {row}")

with open(csv_file2, 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            precip = float(row['precip'])
            tobs = float(row['tobs'])
            cursor.execute('''
            INSERT OR IGNORE INTO measurements (station, date, precip, tobs)
            VALUES (?, ?, ?, ?)
            ''', (row['station'], row['date'], precip, tobs))
        except ValueError as e:
            print(f"Error in measurements table: {e} for row {row}")

conn.commit()
conn.close()

print('Done')