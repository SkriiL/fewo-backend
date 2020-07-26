import sqlite3
import date


def get_all():
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute('SELECT * FROM comments')
    comments = c.fetchall()
    comments_dict = []
    conn.close()
    for p in comments:
        comments_dict.append({'name': p[0], 'text': p[1], "dateCreated": date.string_to_date(p[2]), 'id': p[3]})
    return comments_dict


def add(comment):
    _id = comment["id"]
    if comment["id"] == -1:
        _id = len(get_all()) + 1
        comments = get_all()
        ids = [c['id'] for c in comments]
        correct = False
        while not correct:
            if _id in ids:
                _id += 1
            else:
                break
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    params = (comment["name"], comment["text"], date.date_to_string(comment["dateCreated"]), _id)
    c.execute('INSERT INTO comments VALUES(?, ?, ?, ?)', params)
    conn.commit()
    conn.close()


def delete(_id):
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    params = (_id,)
    c.execute('DELETE FROM comments WHERE id=?', params)
    conn.commit()
    conn.close()


def edit(comment):
    delete(int(comment["id"]))
    add(comment)
