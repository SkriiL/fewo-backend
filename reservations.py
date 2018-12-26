import sqlite3


def get_all():
    conn = sqlite3.connect('../fewo-backend/db.db')
    c = conn.cursor()
    c.execute('SELECT * FROM reservations')
    reservations = c.fetchall()
    conn.close()
    res_dir = []
    for r in reservations:
        res_dir.append({'name': r[0], 'dateFrom': r[1], 'dateTo': r[2], 'count': r[3], 'email': r[4], 'phone': r[5],
                        'street': r[6], 'houseNumber': r[7], 'city': r[8], 'postalCode': r[9], 'country': r[10], 'id': r[11]})
    return res_dir


def add(res_str, id=len(get_all()) + 1):
    res = res_str.split('|')
    conn = sqlite3.connect('../fewo-backend/db.db')
    c = conn.cursor()
    params = (res[0], res[1], res[2], int(res[3]), res[4], res[5], res[6], res[7], res[8], int(res[9]), res[10], id)
    c.execute('INSERT INTO reservations VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', params)
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect('../fewo-backend/db.db')
    c = conn.cursor()
    params = (id,)
    c.execute('DELETE FROM reservations WHERE id=?', params)
    conn.commit()
    conn.close()


def edit(res_str):
    res = res_str.split('|')
    delete(int(res[11]))
    add(res_str, int(res[11]))