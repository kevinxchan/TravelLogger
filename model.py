from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from DateConverter import DateConverter
from werkzeug.security import generate_password_hash, check_password_hash

ma = Marshmallow()
db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    countries = db.relationship('Visit', back_populates='user')

    def __init__(self, username, password, first_name='', last_name=''):
        self.username = username
        self.password = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Country(db.Model):
    __tablename__ = 'Country'
    id = db.Column(db.String(2), primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    users = db.relationship('Visit', back_populates='country')

    def __init__(self, _id, name):
        self.id = _id
        self.name = name


class Visit(db.Model):
    __tablename__ = 'Visit'
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True, onupdate='CASCADE')
    country_id = db.Column(db.String(2), db.ForeignKey('Country.id'), primary_key=True, onupdate='CASCADE')
    year = db.Column(db.String(4), server_default=DateConverter.get_current_day_string())
    month = db.Column(db.String(2), server_default=DateConverter.get_current_month_string())
    day = db.Column(db.String(2), server_default=DateConverter.get_current_day_string())

    user = db.relationship('User', back_populates='countries')
    country = db.relationship('Country', back_populates='users')

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(min=3))
    password = fields.String(required=True, validate=validate.Length(min=6))
    first_name = fields.String()
    last_name = fields.String()
    creation_date = fields.DateTime()


class CountrySchema(ma.Schema):
    id = fields.String(validate=validate.Length(min=2, max=2))
    name = fields.String(validate=validate.Length(min=4))


class VisitSchema(ma.Schema):
    user_id = fields.Integer(dump_only=True, required=True)
    country_id = fields.String(dump_only=True, required=True)
    year = fields.String()
    month = fields.String()
    day = fields.String()
