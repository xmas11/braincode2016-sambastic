from subprocess import call
from settings import *
from flaskapp import db, User, user_datastore

call(["rm", "db.sqlite3"])

db.create_all()

user_datastore.create_user(email=USER_EMAIL, password=USER_PASSWORD)
db.session.commit()
