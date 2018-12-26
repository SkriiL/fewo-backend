import sqlite3


def get_all():
    conn = sqlite3.connect('../fewo-backend/db.db')
    c = conn.cursor()
    c.execute('SELECT * FROM prices')
    prices = c.fetchall()
    prices_dict = []
    for p in prices:
        prices_dict.append({'id': p[0], 'label': p[1], 'price': p[2]})
    return prices_dict


def add(price_str, id=len(get_all()) + 1):
    price = price_str.split('|')
    conn = sqlite3.connect('../fewo-backend/db.db')
    c = conn.cursor()
    params = (id, price[1], price[2])
    c.execute('INSERT INTO prices VALUES(?, ?, ?)', params)
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect('../fewo-backend/db.db')
    c = conn.cursor()
    params = (id,)
    c.execute('DELETE FROM prices WHERE id=?', params)
    conn.commit()
    conn.close()


def edit(price_str):
    price = price_str.split('|')
    delete(int(price[0]))
    add(price_str, int(price[0]))