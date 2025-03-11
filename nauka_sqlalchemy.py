from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db', echo=True)

meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String),
   Column('lastname', String),
)

meta.create_all(engine)
print("Table created")

from sqlalchemy import students
ins = students.insert()
# ins = <sqlalchemy.sql.dml.Insert object at 0x7105489348>
str(ins)
'INSERT INTO students (id, name, lastname) VALUES (:id, :name, :lastname)'

ins.compile().params
{'id': None, 'name': None, 'lastname': None}
ins = students.insert().values(name='Eric', lastname='Idle')
ins.compile().params
{'name': 'Eric', 'lastname': 'Idle'}