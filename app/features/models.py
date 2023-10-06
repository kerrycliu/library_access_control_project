from flask_sqlalchemy import SQLAlchemy
from app import login,db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False, unique=True)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def set_password(self, password):
        self.password = generate_password_hash(password)
'''
class rent_books(db.Model):
    id=
    username
    bookname
    returndate
'''

@login.user_loader
def load_user(id):
    return user.query.get(int(id))
