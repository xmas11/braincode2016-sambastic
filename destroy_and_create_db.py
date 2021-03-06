from subprocess import call
from settings import *
from flaskapp import *

call(["rm", "db.sqlite3"])

db.create_all()
session = db.session

user_datastore.create_user(email=USER_EMAIL, password=USER_PASSWORD)
session.commit()
user = User.query.filter(User.email==USER_EMAIL).first()

tracker = Tracker(name='Tracker 1', query_string='lenovo')
empty_tracker = Tracker(name='Tracker 2', query_string='macbook')
session.add(tracker)
session.add(empty_tracker)

offer = Offer(offer_id='offer_1', title='Offer 1')
session.add(offer)

user_offer = UserOffer(user=user, offer=offer, status="not_viewed")
session.add(user_offer)

offer_tracker = TrackerOffer(offer=offer, tracker=tracker)
session.add(offer_tracker)

user_tracker = UserTracker(user=user, tracker=tracker)

session.commit()

for user_tracker in user.trackers:
    print(user_tracker.tracker.name, user_tracker.tracker.id)

for tracker_offer in tracker.offers:
    print(tracker_offer.offer.title, tracker_offer.offer.offer_id)





