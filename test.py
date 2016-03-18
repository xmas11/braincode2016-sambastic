import requests
import json

API_KEY = "93f25f292141e6824da2a235edcf59292d69febaa06d0798e80905ba440201b6"

def getthinkpad():
        headers = {'content-type': 'application/json'}
        t = requests.post(
                'http://api.natelefon.pl/v2/allegro/offers?access_token=93f25f292141e6824da2a235edcf59292d69febaa06d0798e80905ba440201b6',
                data=json.dumps(
                        {
                                "access_token": "93f25f292141e6824da2a235edcf59292d69febaa06d0798e80905ba440201b6",
                                "searchString": "Thinkpad X230"
                        }),
                headers=headers
        )
        return t.json()


class Offer:

        def __init__(self):
                self.key = API_KEY #API key hardcoded

        def query(self, query_string, min_price=100, max_price=1000):
                headers = {'content-type': 'application/json'}
                t = requests.post(
                        'http://api.natelefon.pl/v2/allegro/offers?access_token='+API_KEY,
                        data=json.dumps(
                                {
                                        "access_token": API_KEY,
                                        "searchString": query_string
                                }),
                        headers=headers
                )
                return t.json()
