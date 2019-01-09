import sqlite3
from crypto import OneTimePad


def get_all():
    conn = sqlite3.connect('../fewo-backend/db.db')
    c = conn.cursor()
    c.execute('SELECT * FROM passwords')
    results = c.fetchall()
    passwords = []
    conn.close()
    for r in results:
        pw_list = r[0].split('|')
        key_list = r[1].split('|')
        pw_bin = OneTimePad.decrypt(pw_list, key_list)
        passwords.append({'password': OneTimePad.bin_to_word(pw_bin), 'name': r[2]})
    return passwords


def login(pwd):
    pws = get_all()
    name = '-1'
    for pw in pws:
        if pw['password'] == pwd:
            name = pw['name']
    return name


def add_password(pwd, name):
    o = OneTimePad(pwd)
    result = o.encrypt()
    result_word = []
    for item in result:
        string = ''
        for letter in item:
            string += letter + '|'
        result_word.append(string[:-1])

    conn = sqlite3.connect('../fewo-backend/db.db')
    c = conn.cursor()
    params = (result_word[0], result_word[1], name)
    c.execute('INSERT INTO passwords VALUES(?, ?, ?)', params)
    conn.commit()
    conn.close()