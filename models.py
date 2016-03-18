from flaskapp import db
from settings import *


class Category(db.Model):
    name = db.Column(db.String(STR_LEN))
    parent = db.relationship("Category", backref="child")

class AllegroUser(db.Model):
    login = db.Column(db.String(STR_LEN), primary_key=True)

class Offer(db.Model):
    id = db.Column(db.String(STR_LEN), primary_key=True)
    title = db.Column(db.String(STR_LEN))
    price = db.Column(db.Integer)

    def log_offer(self):
        """
            Logs previous offer data.
        """
        pass

class Bid(db.Model):
    pass

class Purchase(db.Model):
    pass

class OfferLog(db.Model):
    pass

class Product(db.Model):
    pass

class ProductOffers(db.Model):
    pass

class ProductFilter(db.Model):
    pass


