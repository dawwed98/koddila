import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def execute_sql(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(e)

database = r"movies.db"
database2 = r"platform.db"

sql_create_movies_table = """
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    year INTEGER,
    genre TEXT,
    platform TEXT,
    FOREIGN KEY (platform) REFERENCES platform(name)
);
"""

sql_create_platform_table = """
CREATE TABLE IF NOT EXISTS platform (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    cost REAL,
    type TEXT,
    FOREIGN KEY (name) REFERENCES movies(platform)
);
"""

sql_insert_movies = """
INSERT INTO movies (title, year, genre, platform) VALUES
('Pulp Fiction', 1994, 'crime', 'Netflix'),
('Matrix', 1999, 'sci-fi', 'HBO'),
('The Simpsons', 1989, 'animation', 'Disney+'),
('Friends', 1994, 'comedy', 'Netflix'),
('Game of Thrones', 2011, 'fantasy', 'HBO');
"""

sql_insert_platform = """
INSERT INTO platform (name, cost, type) VALUES 
('Netflix', 10, 'streaming'),
('HBO', 15, 'streaming'),
('Disney+', 8, 'streaming');
"""
update_sql = """
UPDATE movies
SET platform = 'Disney+'
WHERE title = 'Friends';
"""

conn = create_connection(database)
conn2 = create_connection(database2)

if conn is not None:
    execute_sql(conn, sql_create_movies_table)
    execute_sql(conn, sql_insert_movies)
    execute_sql(conn2, sql_create_platform_table)
    execute_sql(conn2, sql_insert_platform)
    execute_sql(conn, update_sql)
else:
    print("Nie można połączyć się z bazą danych.")

