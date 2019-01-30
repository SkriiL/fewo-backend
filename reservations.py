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


def get_single(id):
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    params = (int(id),)
    c.execute('SELECT * FROM reservations WHERE id=?', params)
    r = c.fetchone()
    res = {'name': r[0], 'dateFrom': r[1], 'dateTo': r[2], 'count': r[3], 'price': r[4], 'email': r[5], 'phone': r[6],
           'street': r[7], 'houseNumber': r[8], 'city': r[9], 'postalCode': r[10], 'country': r[11], 'id': r[12],
           'nationality': r[13], 'isSameAsNormal': r[14], 'billStreet': r[15], 'billHouseNumber': r[16],
           'billCity': r[17], 'billPostalCode': r[18], 'billCountry': r[19], 'companyName': r[20]}
    conn.close()
    return res


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


class Reservation:
    def __init__(self):
        self.name = ""
        self.dateFrom = ""
        self.dateTo = ""
        self.count = -1
        self.price = ""
        self.email = ""
        self.phone = ""
        self.street = ""
        self.houseNumber = ""
        self.city = ""
        self.postalCode = ""
        self.country = ""
        self.id = -1
        self.nationality = ""
        self.isSameAsNormal = False
        self.billStreet = ""
        self.billHouseNumber = ""
        self.billCity = ""
        self.billPostalCode = ""
        self.billCountry = ""
        self.companyName = ""

    def values_to_model(self, res):
        self.name = res["name"]
        self.dateFrom = res["dateFrom"]
        self.dateTo = res["dateTo"]
        self.count = res["count"]
        self.price = res["price"]
        self.email = res["email"]
        self.phone = res["phone"]
        self.street = res["street"]
        self.houseNumber = res["houseNumber"]
        self.city = res["city"]
        self.postalCode = res["postalCode"]
        self.country = res["country"]
        self.id = res["id"]
        self.nationality = res["nationality"]
        print(self.isSameAsNormal)
        if res['isSameAsNormal'] == 'true':
            self.isSameAsNormal = True
        else:
            self.isSameAsNormal = False
        self.billStreet = res["billStreet"]
        self.billHouseNumber = res["billHouseNumber"]
        self.billCity = res["billCity"]
        self.billPostalCode = res["billPostalCode"]
        self.billCountry = res["billCountry"]
        self.companyName = res["companyName"]
