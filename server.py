from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from OpenSSL import SSL
import socketio
import engineio
import eventlet
import eventlet.wsgi
import reservations
import login
import prices

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret!"
sio = SocketIO(app)


@app.route("/")
def index():
    return app.send_static_file('index.html')


@sio.on('connect')
def connect():
    print(request.sid + " connected")


@sio.on('login')
def login_(pw):
    print("Hallo")
    name = login.login(pw)
    send_name(name)


def send_name(name):
    emit('loggedIn', name)


# !!!!!!!!!!!!!!!!!!!!!!!!! RESERVATIONS !!!!!!!!!!!!!!!!!!!


@sio.on('getAllReservations')
def get_all_reservations(arg):
    res = reservations.get_all()
    send_reservations(res)


def send_reservations(res):
    emit('reservations', res)


@sio.on('getAllCalReservations')
def get_all_cal_reservations(arg):
    res = reservations.get_all()
    send_reservations_cal(res)


def send_reservations_cal(res):
    emit('reservationsCal', res)


@sio.on('addReservation')
def add_reservation(res):
    reservations.add(res)


@sio.on('editReservation')
def edit_reservation(res):
    reservations.edit(res)


@sio.on('deleteReservation')
def delete_reservation(id):
    reservations.delete(int(id))


# !!!!!!!!!!!!!!!!!!!!!!!!! RESERVATIONS !!!!!!!!!!!!!!!!!!!


@sio.on('getAllPrices')
def get_all_prices(sid):
    ps = prices.get_all()
    send_prices(ps)


def send_prices(ps):
    emit('prices', ps)


@sio.on('addPrice')
def add_price(p):
    prices.add(price_str=p)


@sio.on('editPrice')
def edit_price(p):
    prices.edit(p)


@sio.on('deletePrice')
def delete_price(id):
    prices.delete(int(id))


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


if __name__ == '__main__':
    try:
        eventlet.wsgi.server(eventlet.wrap_ssl(eventlet.listen(('', 56789)),
                                               certfile='../fewogrimm.de_ssl_certificate.cer',
                                               keyfile="../_.fewogrimm.de_private_key.key",
                                               server_side=True), app)
    except Exception as e:
        print("Fehler")
    # sio.run(app, port=56789, host="0.0.0.0")
