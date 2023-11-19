from flask_sqlalchemy import SQLAlchemy
from app import login,db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Defines user information
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def set_password(self, password):
        self.password = generate_password_hash(password)

# Defines book checkout information
class Rent_books(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),nullable=True)
    bookname = db.Column(db.String(100), nullable=True)
    returndate = db.Column(db.DateTime, nullable=False)

# Defines book database information
class Book_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_ttl = db.Column(db.String(100),nullable=False)
    book_gere = db.Column(db.String(100), nullable=False)
    book_aval = db.Column(db.Boolean, nullable=True)

# Defines Delete user:
class Delete_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=True)
    admin_username = db.Column(db.String(100), nullable=False)
    deleted_user = db.Column(db.String(100), nullable=False)
    delete_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    admin_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    admin = db.relationship('User', foreign_keys=[admin_id], backref='deleted_by_admin', uselist=False)
    user = db.relationship('User', foreign_keys=[user_id], backref='deleted_user', uselist=False)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
