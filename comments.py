import sqlite3


def get_all():
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute('SELECT * FROM comments')
    comments = c.fetchall()
    comments_dict = []
    conn.close()
    for p in comments:
        comments_dict.append({'name': p[0], 'text': p[1], "dateCreated": p[2], 'id': p[3]})
    return comments_dict


def add(comment_str, _id=-1):
    if _id == -1:
        _id = len(get_all()) + 1
        comments = get_all()
        ids = [c['id'] for c in comments]
        correct = False
        while not correct:
            if _id in ids:
                _id += 1
            else:
                break
    comment = comment_str.split('|')
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    params = (comment[0], comment[1], comment[2], _id)
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


def edit(comment_str):
    comment = comment_str.split('|')
    delete(int(comment[3]))
    add(comment_str, int(comment[3]))