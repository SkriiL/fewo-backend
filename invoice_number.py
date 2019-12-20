import datetime
import sqlite3


def get_year():
    return datetime.datetime.now().year


def new(year, number):
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    deleteParams = (year, )
    insertParams = (year, number, )
    c.execute('DELETE FROM invoiceNumbers WHERE year=?', deleteParams)
    c.execute('INSERT INTO invoiceNumbers VALUES(?,?)', insertParams)
    conn.commit()
    conn.close()


def get_current(year):
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    params = (year, )
    c.execute('SELECT * FROM invoiceNumbers WHERE year=?', params)
    arr = c.fetchone()
    conn.close()
    num = 1
    if arr is not None:
        num = int(arr[1]) + 1
    new(int(year), num)
    if num < 10:
        return "00" + str(num)
    elif 10 <= num < 100:
        return "0" + str(num)
    elif 100 <= num < 1000:
        return str(num)


def get_invoice_number():
    year = int(get_year())
    num = get_current(year)
    return "RE-" + str(year) + "-" + num