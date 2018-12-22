import sqlite3


def get_all():
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute('SELECT * FROM reservations')
    reservations = c.fetchall()
    conn.close()
    res_dir = []
    for r in reservations:
        res_dir.append({'name': r[0], 'dateFrom': r[1], 'dateTo': r[2]})
    return res_dir


def add(res_str):
    res = res_str.split('|')
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    params = (res[0], res[1], res[2],)
    c.execute('INSERT INTO reservations VALUES(?, ?, ?)', params)
    conn.commit()
    conn.close()
