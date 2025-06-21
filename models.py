from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    pw_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, pw):
        self.pw_hash = generate_password_hash(pw)
    def check_password(self, pw):
        return check_password_hash(self.pw_hash, pw)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer)
    diagnosis = db.Column(db.String(255))
