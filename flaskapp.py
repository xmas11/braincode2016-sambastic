import datetime
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
from sqlalchemy import event, desc
from settings import *
from api_helper import ApiHelper
from matplotlib import pyplot as plt

import os
import sys
import logging

import hashlib
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

"""***********  User management  ************"""

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    offers = db.relationship("UserOffer")

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

""" ******************  Models  ******************** """

class Category(db.Model):
    name = db.Column(db.String(STR_LEN), primary_key=True)
    #parent = db.relationship('Category', backref='children')
    #parent_name = db.Column(db.String(STR_LEN), db.ForeignKey('category.name'))

class AllegroUser(db.Model):
    THRESHOLDS = [5, 50, 250, 2500, 12500, 1e9]
    login = db.Column(db.String(STR_LEN), primary_key=True)
    rating = db.Column(db.Integer)

    @classmethod
    def user_rating_class(cls, rating):
        rclass = 0
        for threshold in cls.THRESHOLDS:
            if rating < threshold:
                return rclass
            rclass += 1

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
    cheapest_shipment = db.Column(db.Integer)
    bids_number = db.Column(db.Integer)

    published_dt = db.Column(db.DateTime)
    end_dt = db.Column(db.DateTime)
    changed_dt = db.Column(db.DateTime)
    sold_dt = db.Column(db.DateTime)

class UserOffer(db.Model):
    offer_id = db.Column(db.String(STR_LEN), db.ForeignKey('offer.offer_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    offer = db.relationship("Offer")
    status = db.Column(db.Integer)
    last_seen = db.Column(db.DateTime)

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
    created_at_dt = db.Column(db.DateTime, primary_key=True)


"""
class Product(db.Model):
    pass

class ProductOffers(db.Model):
    pass

class ProductFilter(db.Model):
    pass
"""
# standard decorator style

def on_offer_field_change(field):
    def _on_field_change(offer, value, old_value, initiator):
        if offer.offer_id and value != old_value and old_value is not None:
            log = OfferLog(offer=offer)
            log.offer_id = offer.offer_id
            setattr(log, field, old_value)
            print('creating log', vars(log))
            db.session.add(log)
            db.session.commit()
    return _on_field_change

event.listen(Offer.buy_now_price, 'set', on_offer_field_change('buy_now_price'))
event.listen(Offer.end_dt, 'set', on_offer_field_change('end_dt'))
event.listen(Offer.highest_bid_amount, 'set', on_offer_field_change('highest_bid_amount'))

"""
@event.listens_for(Offer, 'before_update')
def on_before_update(mapper, connection, offer):
    if offer and offer.offer_id:
        fields = ['offer_id', 'buy_now_price', 'end_dt', 'highest_bid_amount']
        last_log = OfferLog.query.order_by(desc('created_at_dt')).first()
        if (not last_log) or any(getattr(last_log, field) != getattr(offer, field) for field in fields):
            log = OfferLog(offer=offer)
            for field in fields:
                setattr(log, field, getattr(offer, field))
            print('creating log', vars(log))
            db.session.add(log)
            db.session.commit()
"""

@event.listens_for(OfferLog, 'before_insert')
def on_offer_log_insert(mapper, connection, offer_log):
    offer_log.created_at_dt = datetime.datetime.now()

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@login_required
@app.route("/")
def index():
    return app.send_static_file('index.html')

@login_required
@app.route("/mvp/<query>")
def mvp(query):
    offers = list(ApiHelper.request_offers(query_string=query,
                                      min_price=100,
                                      max_price=3000))
    prices = []
    for offer in offers:
        if(offer['prices']['buyNow']>300):
            prices.append(offer['prices']['buyNow'])
    plt.figure(1)
    plt.hist(prices, bins=20)
    m=hashlib.md5()
    m.update(query)
    hash = str(int(time.time()))
    plt.savefig('static/histogram'+hash+'.png')
    return render_template("mvp.html", offers=offers, hash=hash, req=query)

if __name__ == '__main__':
    app.run(debug=True)
