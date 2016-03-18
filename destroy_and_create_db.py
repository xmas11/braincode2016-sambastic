from subprocess import call
call(["rm", "db.sqlite3"])

from flaskapp import db
db.create_all()
