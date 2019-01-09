from aiohttp import web
import socketio
import reservations
import login
import prices

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


@sio.on('connect')
def connect(sid, environ):
    print(sid + " connected")
    sio.enter_room(sid, room='standard')


@sio.on('login')
async def login_(sid, pw):
    name = login.login(pw)
    await send_name(sid, name)


async def send_name(sid, name):
    await sio.emit('loggedIn', name, room=sid)


# !!!!!!!!!!!!!!!!!!!!!!!!! RESERVATIONS !!!!!!!!!!!!!!!!!!!


@sio.on('getAllReservations')
async def get_all_reservations(sid, arg):
    res = reservations.get_all()
    await send_reservations(sid, res)


async def send_reservations(sid, res):
    await sio.emit('reservations', res, room=sid)


@sio.on('addReservation')
async def add_reservation(sid, res):
    reservations.add(res)


@sio.on('editReservation')
async def edit_reservation(sid, res):
    reservations.edit(res)


@sio.on('deleteReservation')
async def delete_reservation(sid, id):
    reservations.delete(int(id))


# !!!!!!!!!!!!!!!!!!!!!!!!! RESERVATIONS !!!!!!!!!!!!!!!!!!!


@sio.on('getAllPrices')
async def get_all_prices(sid, arg):
    ps = prices.get_all()
    await send_prices(sid, ps)


async def send_prices(sid, ps):
    await sio.emit('prices', ps, room=sid)


@sio.on('addPrice')
async def add_price(sid, p):
    prices.add(price_str=p)


@sio.on('editPrice')
async def edit_price(sid, p):
    prices.edit(p)


@sio.on('deletePrice')
async def delete_price(sid, id):
    prices.delete(int(id))


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app, port='56789')