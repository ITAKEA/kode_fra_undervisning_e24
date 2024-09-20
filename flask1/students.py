import sqlite3
from data_dict import random_users

def create():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT)')
        cur.execute("INSERT INTO students VALUES (1, 'Claus')")
        cur.execute("INSERT INTO students VALUES (2, 'Torben')")
        cur.execute("INSERT INTO students VALUES (3, 'Anna')")

def read():
    students = []

    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM students')

        for i in cur.fetchall():
            students.append({'id' : i[0], 'name' : i[1]})

    return students



def create():
    with sqlite3.connect('school.db') as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS members (id INTEGER, name TEXT)')
        cur.executemany('INSERT INTO members VALUES(?,?,?,?,?,?,?,?,?)', random_users)