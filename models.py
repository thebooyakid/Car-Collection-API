from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

db = SQLAlchemy()

class User(db.Model):
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


