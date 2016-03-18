from flaskapp import db
from settings import *


class Category(db.Model):
    name = db.Column(db.String(STR_LEN))
    parent = db.relationship("Category", backref="child")

class AllegroUser(db.Model):
    login = db.Column(db.String(STR_LEN), primary_key=True)

class Offer(db.Model):
    id = db.Column(db.String(STR_LEN), primary_key=True)
    title = db.Column(db.Text)
    seller = db.relationship('AllegroUser')
    url = db.Column(db.String(STR_LEN))

    sold = db.Column(db.Boolean)
    finished = db.Column(db.Boolean)

    buy_now_price = db.Column(db.Integer)
    highest_bid_amount = db.Column(db.Integer)
    sold_price = db.Column(db.Integer)

    published_dt = db.Column(db.DateTime)
    end_dt = db.Column(db.DateTime)
    changed_dt = db.Column(db.DateTime)
    sold_dt = db.Column(db.DateTime)

    def log_offer(self):
        """
            Logs previous offer data.
        """
        pass

class Bid(db.Model):
    user = db.relationship('AllegroUser', backref="bids")
    offer = db.relationship("Offer", backref="bids")
    amount = db.Column(db.Integer)
    dt = db.Column(db.DateTime)

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


