from flask import Flask
from flask_socketio import SocketIO, emit

from reminders import *

# App exist in setting
# app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('get_reminders')
def socket_get_reminders():
    print('Get reminders with API')
    data = Reminder.get_all_reminders()
    emit('reminders_response', {'data': data})


if __name__ == '__main__':
    socketio.run(app, port=8000)