import sqlite3
import date


def get_all():
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute('SELECT * FROM reservations')
    reservations = c.fetchall()
    conn.close()
    res_dir = []
    for r in reservations:
        res_dir.append({'name': r[0], 'dateFrom': date.string_to_date(r[1]), 'dateTo': date.string_to_date(r[2]),
                        'count': r[3], 'price': r[4], 'email': r[5], 'phone': r[6], 'street': r[7], 'houseNumber': r[8],
                        'city': r[9], 'postalCode': r[10], 'country': r[11], 'id': r[12], 'nationality': r[13],
                        'isSameAsNormal': r[14], 'billStreet': r[15], 'billHouseNumber': r[16], 'billCity': r[17],
                        'billPostalCode': r[18], 'billCountry': r[19], 'companyName': r[20], "invoiceType": r[21],
                        "invoiceNumber": r[22]})
    return res_dir


def get_single(id):
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    params = (int(id),)
    c.execute('SELECT * FROM reservations WHERE id=?', params)
    r = c.fetchone()
    res = {'name': r[0], 'dateFrom': date.string_to_date(r[1]), 'dateTo': date.string_to_date(r[2]), 'count': r[3],
           'price': r[4], 'email': r[5], 'phone': r[6], 'street': r[7], 'houseNumber': r[8], 'city': r[9],
           'postalCode': r[10], 'country': r[11], 'id': r[12], 'nationality': r[13], 'isSameAsNormal': r[14],
           'billStreet': r[15], 'billHouseNumber': r[16], 'billCity': r[17], 'billPostalCode': r[18],
           'billCountry': r[19], 'companyName': r[20], "invoiceType": r[21], 'invoiceNumber': r[22]}
    conn.close()
    return res


def add(res):
    id = res["id"]
    if id == -1:
        id = len(get_all()) + 1
        ress = get_all()
        ids = [r['id'] for r in ress]
        correct = False
        while not correct:
            if id in ids:
                id += 1
            else:
                break
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    invoice_number = "-1"
    try:
        if res["invoiceNumber"] is not None:
            invoice_number = res[22]
    except:
        invoice_number = "-1"
    params = (res["name"], date.date_to_string(res["dateFrom"]), date.date_to_string(res["dateTo"]), int(res["count"]),
              res["price"], res["email"], res["phone"], res["street"], res["houseNumber"], res["city"],
              res["postalCode"], res["country"], id, res["nationality"], res["isSameAsNormalString"], res["billStreet"],
              res["billHouseNumber"], res["billCity"], res["billPostalCode"], res["billCountry"], res["companyName"],
              res["invoiceType"], invoice_number)
    c.execute('INSERT INTO reservations VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', params)
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    params = (id,)
    c.execute('DELETE FROM reservations WHERE id=?', params)
    conn.commit()
    conn.close()


def edit(res):
    delete(int(res["id"]))
    add(res)


def set_invoice_number(id, invoice_number):
    res = get_single(id)
    res['invoiceNumber'] = invoice_number
    delete(id)
    add(res)


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
        self.invoiceType = ""
        self.invoiceNumber = ""

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
        self.invoiceType = res["invoiceType"]
        self.invoiceNumber = res["invoiceNumber"]
