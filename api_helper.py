import requests
import json
from app_exceptions import ApiException

from settings import API_KEY

OFFERS_URL = 'http://api.natelefon.pl/v2/allegro/offers?access_token=%s' % API_KEY

class ApiHelper(object):

    HEADERS = {'content-type': 'application/json'}

    @classmethod
    def request_offers(cls, query_string, min_price=100, max_price=1000):
        return cls._post(OFFERS_URL, searchString=query_string)

    @classmethod
    def _post(cls, url, *args, **kwargs):
        kwargs["access_token"] = API_KEY
        print(kwargs)
        resp = requests.post(url, data=json.dumps(kwargs), headers=cls.HEADERS)
        if resp.ok:
            return resp.json()
        else:
            raise ApiException("ERROR in calling %s, reason: %s" % (url, resp.reason))


