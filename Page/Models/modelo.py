from Page import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  #'primary_key'
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Integer, nullable=False, default=1)
    created_on = db.Column(db.DateTime, default=datetime.now)  # DateTime'

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<user:{self.username}>'


class Tareas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 'primary_key'
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text)
    state = db.Column(db.Boolean, default=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  #  'Integer' y 'ForeignKey'
    is_active = db.Column(db.Integer, nullable=False, default=1)
    created_on = db.Column(db.DateTime, default=datetime.now)  # 'DateTime'

    def __init__(self, title, desc, state,created_by):
        self.title = title
        self.desc = desc
        self.state = state
        self.created_by = created_by


    def __repr__(self):
        return f'<tarea:{self.title}>'
