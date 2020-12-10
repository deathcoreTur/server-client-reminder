from socketIO_client import SocketIO, LoggingNamespace


def reminders_response(args):
    print('Reminders', args['data'])


def added_new_reminder_response(args):
    print('New reminder is', args['data'])


socketIO = SocketIO('localhost', 8000, LoggingNamespace)

socketIO.on('reminders_response', reminders_response)
socketIO.emit('get_reminders')

# NEED TO WRITE SOCKET which help me listen adding Reminder
# socketIO.on('added_new_reminder_response', added_new_reminder_response)
# socketIO.emit('')
socketIO.wait(seconds=10)
