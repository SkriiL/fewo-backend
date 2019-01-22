from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from OpenSSL import SSL
import ssl
import socketio
import reservations
import eventlet
import login
import prices

app = Flask(__name__)
#app.config['SECRET_KEY'] = "secret!"
sio = SocketIO(app)

eventlet.monkey_patch()


@app.route("/")
def index():
    return app.send_static_file('index.html')


@sio.on('connect')
def connect():
    print(request.sid + " connected")


@sio.on('login')
def login_(pw):
    print("Hallo")
    name = login.login(pw['data'])
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
    reservations.add(res['data'])


@sio.on('editReservation')
def edit_reservation(res):
    reservations.edit(res['data'])


@sio.on('deleteReservation')
def delete_reservation(id):
    reservations.delete(int(id['data']))


# !!!!!!!!!!!!!!!!!!!!!!!!! RESERVATIONS !!!!!!!!!!!!!!!!!!!


@sio.on('getAllPrices')
def get_all_prices(sid):
    ps = prices.get_all()
    send_prices(ps)


def send_prices(ps):
    emit('prices', ps)


@sio.on('addPrice')
def add_price(p):
    prices.add(price_str=p['data'])


@sio.on('editPrice')
def edit_price(p):
    prices.edit(p['data'])


@sio.on('deletePrice')
def delete_price(id):
    prices.delete(int(id['data']))


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


context = ("../fewogrimm.de_ssl_certificate.cer", "../_.fewogrimm.de_private_key.key")

if __name__ == '__main__':
    #eventlet.wsgi.server(eventlet.wrap_ssl(eventlet.listen(('', 56789)),
    #                                       certfile='cert.crt',
    #                                       keyfile="private.key",
    #                                       server_side=True), app)
    eventlet.wrap_ssl(sio.run(app, port=56789, host="0.0.0.0", debug=True), keyfile="../_.fewogrimm.de_private_key.key", certfile="../fewogrimm.de_ssl_certificate.cer", server_side=True)
