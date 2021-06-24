from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from flask_login import UserMixin, LoginManager
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    first_name = db.Column(db.String(150), nullable = True, default='')
    last_name = db.Column(db.String(150), nullable = True, default='')
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = True, default='')
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    token = db.Column(db.String, default = '', unique = True)
    #g_auth_verify

    def __init__(self,email,username = '', first_name = '', last_name = '', id = '', password = ''):
        self.id = self.set_id()
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = self.set_password(password)
        self.token = self.set_token(24)
    
    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def set_token(self, length):
        return secrets.token_hex(length)

    def __repr__(self):
        return f"You're in, {self.username}."

class Car(db.Model):
    id = db.Column(db.String, primary_key = True)
    make = db.Column(db.String(20))
    model = db.Column(db.String(20))
    year = db.Column(db.Numeric(precision=10,scale=2))
    price = db.Column(db.Numeric(precision=10,scale=2))
    mpg = db.Column(db.Numeric(precision=10,scale=2))
    color = db.Column(db.String(20))
    weight = db.Column(db.String(20))
    upgrades = db.Column(db.String(200), nullable = True)
    condition = db.Column(db.String(200))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self,make,model,year,price,mpg,color,weight,upgrades,condition,user_token,id=''):
        self.id = self.set_id()
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.mpg = mpg
        self.color = color
        self.weight = weight
        self.upgrades = upgrades
        self.condition = condition
        self.user_token = user_token

    def set_id(self):
        return(secrets.token_urlsafe())

    def __repr__(self):
        return f"The {year} {make} {model} has been added"


class CarSchema(ma.Schema):
    class Meta:
        fields = ['id','make','model','year','price','mpg','color','weight','upgrades','condition']

car_schema = CarSchema()
cars_schema = CarSchema(many=True)