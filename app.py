import redis
from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
db = redis.StrictRedis('127.0.0.1', 6379, 0)
socketio = SocketIO(app)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/reminders/')
def reminders():
    return render_template('reminders.html')


@app.route('/add')
def add_reminder():
    return render_template('add_reminder.html')


@socketio.on('connect', namespace='/dd')
def ws_conn():
    c = db.incr('connected')
    socketio.emit('msg', {'count': c}, namespace='/dd')


@socketio.on('disconnect', namespace='/dd')
def ws_disconn():
    print('disconnect')
    c = db.decr('connected')
    socketio.emit('msg', {'count': c}, namespace='/dd')


@socketio.on('reminder', namespace='/dd')
def ws_reminder(message):
    db.lpush('list-reminders', message['reminder'])
    # list_reminders = []
    # while (db.llen('list-reminders') != 0):
    #     list_reminders.append(db.lpop('list-reminders').decode("utf-8"))
    socketio.emit('reminder', {'reminder': message['reminder']}, namespace="/dd")


if __name__ == '__main__':
    socketio.run(app, "0.0.0.0", port=5000)