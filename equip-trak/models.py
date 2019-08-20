from sqlalchemy.sql import func
from config import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    user_name = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(45))
    # history = db.relationship('transactions', backref='users', lazy=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())


class Equipment(db.Model):
    __tablename__ = 'equipments'
    id = db.Column(db.Integer, primary_key=True)
    equip_id = db.Column(db.String(45), unique=True)
    manufacture = db.Column(db.String(45))
    model = db.Column(db.String(45))
    serial = db.Column(db.String(45))
    # history = db.relationship('transactions', backref='equipments', lazy=True)
    created_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())


class Transaction(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey(
        'equipments.id'), nullable=False)
    out_time = db.Column(db.DateTime)
    out_user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)
    out_location = db.Column(db.String(45))
    in_time = db.Column(db.DateTime)
    in_user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)
    in_location = db.Column(db.String(45))
    created_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())


class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())


class Condition(db.Model):
    __tablename__ = "condtions"
    id = db.Column(db.Integer, primary_key=True)
    condition = db.Column(db.String(45))
    created_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())


class Status(db.Model):
    __tablename__ = "status"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(45))
    created_on = db.Column(db.DateTime, servetr_default=func.now())
    updated_on = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())
