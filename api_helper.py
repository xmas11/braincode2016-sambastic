import requests
import json
from app_exceptions import ApiException

from settings import API_KEY

OFFER_URL = 'http://api.natelefon.pl/v1/allegro/offers/%(offer_id)s?access_token=%(api_key)s'
OFFERS_URL = 'http://api.natelefon.pl/v2/allegro/offers?access_token=%(api_key)s'
USER_URL = 'http://api.natelefon.pl/v1/allegro/users/%(user_id)s?access_token=%(api_key)s'
CATEGORIES_URL = 'http://api.natelefon.pl/v1/allegro/categories?access_token=%(api_key)s'

def resp_ok(resp):
    if resp.ok:
        return True
    else:
        raise ApiException("ERROR in calling %s, reason: %s" % (resp.url, resp.reason))


class ApiHelper(object):

    HEADERS = {'content-type': 'application/json'}
    DEFAULT_LIMIT = 1000

    @classmethod
    def request_offer(cls, offer_id):
        return cls._get(OFFER_URL % {'api_key': API_KEY, 'offer_id': offer_id})

    @classmethod
    def request_offers(cls, query_string, min_price=None, max_price=None):
        url = OFFERS_URL % {'api_key': API_KEY}
        filters = []
        price_range = {}
        if min_price is not None:
            price_range['min'] = min_price
        if max_price is not None:
            price_range['max'] = max_price
        if price_range:
            filters.append({'id': 'price', 'range': price_range})
        for data in cls._fetch_all(url, searchString=query_string, filters=filters):
            if not data['offers']:
                break
            for offer in data['offers']:
                yield offer

    @classmethod
    def request_user(cls, user_id):
        return cls._get(USER_URL % {'api_key': API_KEY, 'user_id': user_id})

    @classmethod
    def request_categories(cls, parent_category_id=None):
        params = parent_category_id and {'parentCategory': parent_category_id}
        for category in cls._get(CATEGORIES_URL % {'api_key': API_KEY}, params=params):
            yield category

    @classmethod
    def _get(cls, url, params=None):
        params = params or {}
        resp = requests.get(url, params=json.dumps(params))
        if resp_ok(resp):
            return resp.json()

    @classmethod
    def _fetch_all(cls, url,  **kwargs):
        limit = cls.DEFAULT_LIMIT
        params = kwargs.copy()
        params["access_token"] = API_KEY
        params["limit"] = limit
        offset = 0
        results_number = 1e6
        while offset < results_number:
            print("LOG: Calling %s (offset %d)" % (url, offset))
            params['offset'] = offset
            resp = requests.post(url, data=json.dumps(params), headers=cls.HEADERS)
            if resp_ok(resp):
                resp_data = resp.json()
                if 'count' in resp_data:
                    results_number = resp_data['count']
                offset += limit
                yield resp_data


