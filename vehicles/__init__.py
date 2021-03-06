from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager,ma
#import models
from flask_cors import CORS
from flask.json import JSONEncoder
from vehicles.helpers import JSONEncoder


app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

root_db.init_app(app)
migrate = Migrate(app, root_db)
login_manager.init_app(app)
ma.init_app(app)

app.json_encoder = JSONEncoder

CORS(app)




