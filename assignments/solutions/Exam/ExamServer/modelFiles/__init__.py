from flask_sqlalchemy import SQLAlchemy
import os

from ExamServer.controllerFiles import app

# using os library to identify path to the file we are in, and store it in basedir variable
basedir = os.path.abspath(os.path.dirname(__file__))

# I am using flask_sqlalchemy create and use my database
# using basedir variable to find path for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # initializing db with configurations above
