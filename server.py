from aiohttp import web
import socketio
import reservations
import login

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
async def login_(sid, args):
    pwds = login.get_all()
    await send_pwds(sid, pwds)


async def send_pwds(sid, pwds):
    await sio.emit('passwords', pwds, room=sid)


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


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app, port='56789')