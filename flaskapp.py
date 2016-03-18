from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from settings import *
from test import Query

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class Category(db.Model):
    name = db.Column(db.String(STR_LEN), primary_key=True)
    #parent = db.relationship('Category', backref='children')
    #parent_name = db.Column(db.String(STR_LEN), db.ForeignKey('category.name'))

class AllegroUser(db.Model):
    login = db.Column(db.String(STR_LEN), primary_key=True)

class Offer(db.Model):
    offer_id = db.Column(db.String(STR_LEN), primary_key=True)
    title = db.Column(db.Text)
    seller = db.relationship('AllegroUser')
    seller_login = db.Column(db.String(STR_LEN), db.ForeignKey('allegro_user.login'))
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

class Purchase(db.Model):
    offer = db.relationship("Offer", backref="purchases")
    offer_id = db.Column(db.String(STR_LEN), db.ForeignKey('offer.offer_id'), primary_key=True)
    buyer = db.relationship('AllegroUser')
    buyer_login = db.Column(db.String(STR_LEN), db.ForeignKey('allegro_user.login'))
    sold_price = db.Column(db.Integer)
    sold_dt = db.Column(db.DateTime)
    buy_now = db.Column(db.Boolean)

class OfferLog(db.Model):
    offer = db.relationship("Offer", backref="logs")
    offer_id = db.Column(db.String(STR_LEN), db.ForeignKey('offer.offer_id'), primary_key=True)
    highest_bid_amount = db.Column(db.Integer)
    buy_now_price = db.Column(db.Integer)
    end_dt = db.Column(db.DateTime)
    modified_at_dt = db.Column(db.DateTime)

"""
class Product(db.Model):
    pass

class ProductOffers(db.Model):
    pass

class ProductFilter(db.Model):
    pass
"""
# standard decorator style
@event.listens_for(Offer, 'before_update')
def on_offer_update(mapper, connection, target):
    print(target.title)

@app.route("/")
def index():
    return "Sambastic Alle"

@app.route("/mvp")
def mvp():
    q = Query()
    offers = q.query("thinkpad x230")["offers"]
    return render_template("mvp.html", offers=offers)

if __name__ == '__main__':
    app.run(debug=True)
