import sqlite3


def get_all():
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute('SELECT * FROM prices')
    prices = c.fetchall()
    prices_dict = []
    conn.close()
    for p in prices:
        prices_dict.append({'id': p[0], 'title': p[1], 'subtitle': p[2], 'price': p[3], 'priority': p[4]})
    return prices_dict


def add(price_str, _id=-1):
    if _id == -1:
        _id = len(get_all()) + 1
        prices = get_all()
        ids = [p['id'] for p in prices]
        correct = False
        while not correct:
            if _id in ids:
                _id += 1
            else:
                break
    price = price_str.split('|')
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    params = (_id, price[1], price[2], price[3], int(price[4]))
    c.execute('INSERT INTO prices VALUES(?, ?, ?, ?, ?)', params)
    conn.commit()
    conn.close()


def delete(_id):
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    params = (_id,)
    c.execute('DELETE FROM prices WHERE id=?', params)
    conn.commit()
    conn.close()


def edit(price_str):
    price = price_str.split('|')
    delete(int(price[0]))
    add(price_str, int(price[0]))