from datetime import datetime

from reminders import *


@app.route('/reminders', methods=['GET'])
def get_reminders():
    '''Function to get all the reminders in the database'''
    return jsonify({'Reminders': Reminder.get_all_reminders()})


@app.route('/reminders/<int:id>', methods=['GET'])
def get_reminder_by_id(id):
    return_value = Reminder.get(id)
    return jsonify(return_value)


@app.route('/reminders', methods=['POST'])
def add_reminder():
    '''Function to add new reminder to our database'''
    request_data = request.get_json()
    time = datetime.strptime(request_data['time'], '%Y-%m-%d %H:%M:%S')
    Reminder.add(request_data["title"], time)
    response = Response("Reminder added", 201, mimetype='application/json')
    return response


@app.route('/reminders/<int:id>', methods=['PUT'])
def update_reminder(id):
    '''Function to edit reminder in our database using reminder id'''
    request_data = request.get_json()
    time = datetime.strptime(request_data['time'], '%Y-%m-%d %H:%M:%S')
    Reminder.update(id, request_data['title'], time)
    response = Response("Reminder Updated", status=200, mimetype='application/json')
    return response


@app.route('/reminders/<int:id>', methods=['DELETE'])
def remove_movie(id):
    '''Function to delete reminder from our database'''
    Reminder.delete(id)
    response = Response("Reminder Deleted", status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(port=1234, debug=True)