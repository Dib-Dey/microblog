##################################################################################################
#The data that will be stored in the database will be represented by a collection of classes,
# usually called database models. The ORM layer within SQLAlchemy will do the translations required
# to map objects created from these classes into rows in the proper database tables.
################################################################################################
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)