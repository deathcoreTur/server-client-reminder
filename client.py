from socketIO_client import SocketIO, LoggingNamespace


def added_new_reminder_response(args):
    print('New reminder is', args['data'])


socketIO = SocketIO('localhost', 1234, LoggingNamespace)

# Create socket which help me to listen creating new reminder
socketIO.on('added_new_reminder_response', added_new_reminder_response)
socketIO.wait(seconds=10)
