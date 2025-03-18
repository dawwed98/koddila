from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
from sqlalchemy.sql import select
from sqlalchemy.sql import text

engine = create_engine('sqlite:///database.db', echo=True)
meta = MetaData()

Zadanie = Table('zadanie', meta,
                Column('station_id', Integer, ForeignKey('station.station_id')),
                Column('date', String),
                Column('precip', Integer),
                Column('tobs', Integer),
)

Station = Table('station', meta,
                Column('station_id', Integer, primary_key=True),
                Column('latitude', Integer),
                Column('longitude', Integer),
                Column('elevation', Integer),
                Column('name', String),
                Column('country', String),
                Column('state', String),
)

def insert_station(station,latitude,longitude,elevation,name,country,state):
    ins = Station.insert().values(station_id='USC00519397', latitude=21.2716, longitude=-157.8168, elevation=3.0, name='WAIKIKI 717.2', country='US', state='HI')
    ins = Station.insert().values(station_id='USC00513117', latitude=21.4234, longitude=-157.8015, elevation=14.6, name='KANEOHE 838.1', country='US', state='HI')
    conn = engine.connect()
    conn.execute(ins)
    conn.execute("SELECT * FROM station LIMIT 5").fetchall() 
    conn.close()

meta.create_all(engine)
inspector = inspect(engine)
print(inspector.get_table_names())
