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

create_project_sql = """
CREATE TABLE IF NOT EXISTS projects (
    id integer PRIMARY KEY,
    name text NOT NULL,
    start_date text,
    end_date text
);
"""

create_task_sql = """
CREATE TABLE IF NOT EXISTS tasks (
    id integer PRIMARY KEY,
    project_id integer NOT NULL,
    name VARCHAR(250) NOT NULL,
    opis text,
    status VARCHAR(15) NOT NULL,
    start_date text NOT NULL,
    end_date text NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id)
);
"""
insert_project_sql = """
INSERT INTO projects (name, start_date, end_date)
VALUES ('Python', '2019-01-01', '2019-01-30');
"""
insert_project_sql = """
INSERT INTO projects (name, start_date, end_date)
VALUES ('Kurs rysunku', '2019-01-01', '2019-01-30');
"""
def add_project(conn, name, start_date, end_date):
    sql = """ \
    INSERT INTO projects (name, start_date, end_date)
    VALUES (?, ?, ?);
    """
    cur = conn.cursor()
    cur.execute(sql, (name, start_date, end_date))
    return cur.lastrowid

def add_task(conn, project_id, name, opis, status, start_date, end_date):
    sql = """ \
    INSERT INTO tasks (project_id, name, opis, status, start_date, end_date)
    VALUES (?, ?, ?, ?, ?, ?);
    """
    cur = conn.cursor()
    cur.execute(sql, (project_id, name, opis, status, start_date, end_date))
    
    ##conn.commit()
    
    return cur.lastrowid

def update(conn, table, id, **kwargs):
    """
    update status, start_date, end_date of a task
    :param conn:
    :param table: table name
    :param id: row id
    return: 
    """
    parameters = [f"{k} =  ?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values = values + (id,)

    sql = f""" update {table} set {parameters} where id = ? """
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
    except Error as e:
        print(e)

def delete_where(conn, table, **kwargs):
    """"
    """
    qs = []
    values = tuple()
    for k, v in kwargs.items():
        qs.append(f"{k} = ?")
        values += (v,)
    qs = " AND ".join(qs)
    sql = f"DELETE FROM {table} WHERE {qs}"
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()

def delate_all(conn, table):
    """
    """
    sql = f"DELETE FROM {table}"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def select_all(conn, table):
    """
    """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    return rows

def select_where(conn, table, **kwargs):
    """
    """
    qs = []
    values = tuple()
    for k, v in kwargs.items():
        qs.append(f"{k} = ?")
        values += (v,)
    qs = " AND ".join(qs)
    sql = f"SELECT * FROM {table} WHERE {qs}"
    cur = conn.cursor()
    cur.execute(sql, values)
    rows = cur.fetchall()
    return rows

if __name__ == '__main__':
    db_file = 'database.db'
    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, create_project_sql)
        execute_sql(conn, create_task_sql)
        execute_sql(conn, insert_project_sql)
        conn.close()
    else:
        print('Error! cannot create the database connection.')
    pr_id = add_project(conn, "Rysunek", "2019-01-01", "2019-01-30")
    task_id = add_task(conn, pr_id, "Zrobic kreske", "Kreska od lewej do prawej", "aktywny", "2019-01-01", "2019-01-30")
    print(pr_id, task_id)
    conn.commit()
    conn.close()
    
