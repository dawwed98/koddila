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

database = r"students.db"

sql_create_students_table = """
CREATE TABLE IF NOT EXISTS students (
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    average_grade REAL,
    school_year INTEGER,
    olympian BOOLEAN DEFAULT 0
);
"""

sql_insert_students = """
INSERT INTO students (name, surname, average_grade, school_year) VALUES 
('Jan', 'Kowalski', 4.5, 3),
('Anna', 'Nowak', 4.0, 2);
"""

sql_update_student = """
UPDATE students 
SET average_grade = 6
WHERE name = 'Jan' AND surname = 'Kowalski';
"""

sql_add_olympian = """
UPDATE students
SET olympian = 1
WHERE name = 'Jan' AND surname = 'Kowalski';
"""

conn = create_connection(database)

if conn is not None:
    execute_sql(conn, sql_create_students_table)
    execute_sql(conn, sql_insert_students)
    execute_sql(conn, sql_update_student)
    execute_sql(conn, sql_add_olympian)
else:
    print("Error! Cannot create the database connection.")

sql_select_students = """
SELECT * FROM students;
"""