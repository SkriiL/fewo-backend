import sqlite3
from crypto import OneTimePad, Hash


def get_all():
    conn = sqlite3.connect('../fewo-backend/db.db')
    c = conn.cursor()
    c.execute('SELECT * FROM passwords')
    results = c.fetchall()
    passwords = []
    conn.close()
    for r in results:
        passwords.append({'hash': r[0], 'name': r[1]})
    return passwords


def login(pwd):
    h = Hash(pwd)
    hashed = h.get_hash()
    pws = get_all()
    name = '-1'
    for pw in pws:
        if pw['hash'] == hashed:
            name = pw['name']
    return name


def add_password(pwd, name):
    h = Hash(pwd)
    hashed = h.get_hash()
    conn = sqlite3.connect('../fewo-backend/db.db')
    c = conn.cursor()
    params = (hashed, name,)
    c.execute('INSERT INTO passwords VALUES(?, ?)', params)
    conn.commit()
    conn.close()