import json
from settings import *

db = SQLAlchemy(app)


class Reminder(db.Model):
    __tablename__ = 'reminders'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    time = db.Column(db.DateTime, nullable=False)

    def json(self):
        return {'id': self.id, 'title': self.title, 'time': self.time, }

    def add(_title, _time,):
        '''function to add reminder to database using _title, _time
        as parameters'''
        new_reminder = Reminder(title=_title, time=_time)
        db.session.add(new_reminder)
        db.session.commit()

    def get_all_reminders():
        '''function to get all reminders in our database'''
        return [Reminder.json(reminder) for reminder in Reminder.query.all()]

    def get(_id):
        '''function to get reminder using the id of the reminder as parameter'''
        return [Reminder.json(Reminder.query.filter_by(id=_id).first())]

    def update(_id, _title, _time):
        '''function to update the details of a reminder using the id, title,
        time as parameters'''
        reminder_to_update = Reminder.query.filter_by(id=_id).first()
        reminder_to_update.title = _title
        reminder_to_update.time = _time
        db.session.commit()

    def delete(_id):
        '''function to delete a reminder from our database using
           the id of the reminder as a parameter'''
        Reminder.query.filter_by(id=_id).delete()
        db.session.commit()