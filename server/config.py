from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.secret_key = b"\xa1v@\xdc\xc4\x07\xfd\xf6\xd8\x99'\x82z\x17V\xc4"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

metadata = MetaData(naming_convention= {
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
})

db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

bcrypt = Bcrypt(app)

api = Api(app)
CORS(app)

