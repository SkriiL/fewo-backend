import sqlite3


def get_all():
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute('SELECT * FROM reservations')
    reservations = c.fetchall()
    conn.close()
    res_dir = []
    for r in reservations:
        res_dir.append({'name': r[0], 'dateFrom': r[1], 'dateTo': r[2], 'count': r[3], 'price': r[4], 'email': r[5], 'phone': r[6],
                        'street': r[7], 'houseNumber': r[8], 'city': r[9], 'postalCode': r[10], 'country': r[11], 'id': r[12],
                        'nationality': r[13], 'isSameAsNormal': r[14], 'billStreet': r[15], 'billHouseNumber': r[16],
                        'billCity': r[17], 'billPostalCode': r[18], 'billCountry': r[19], 'companyName': r[20]})
    return res_dir


def add(res_str, id=len(get_all()) + 1):
    res = res_str.split('|')
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    params = (res[0], res[1], res[2], int(res[3]), res[4], res[5], res[6], res[7], res[8], res[9], res[10], res[11],
              id, res[13], res[14], res[15], res[16], res[17], res[18], res[19], res[20])
    c.execute('INSERT INTO reservations VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', params)
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    params = (id,)
    c.execute('DELETE FROM reservations WHERE id=?', params)
    conn.commit()
    conn.close()


def edit(res_str):
    res = res_str.split('|')
    delete(int(res[12]))
    add(res_str, int(res[12]))