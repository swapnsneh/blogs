
from flask import Flask
#import psycopg2
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager
#from flask_script import Manager


app = Flask(__name__)
app.config['SECRET_KEY']='mysecret'

####################################
##DATABASE SETUP#################
###############################
#basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/personalblog'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bqenjpxafrpouj:5744485dbf9b0ab74e783ace8cfb69742afe376c94b71fbeb3d866b809397c54@ec2-35-171-250-21.compute-1.amazonaws.com:5432/d2up5por7c23uf?sslmode=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
db.init_app(app)

Migrate(app,db)
#manager = Manager(app)

#manager.add_command('db')

#cursor
#cur = conn.cursor()

#execute query
#cur.execute("select * from users")

#rows = cur.fetchall()

#close the cursor
#cur.close()

#close the connection
#conn.close()

################################
#########LOGIN CONFIGURATION####
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

####################################

from vrbakerblog.core.views import core
from vrbakerblog.users.views import users
from vrbakerblog.blog_posts.views import blog_posts
from vrbakerblog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)
