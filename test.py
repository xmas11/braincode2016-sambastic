import requests

import json

API_KEY = "0e447ed8a0daa0f01f074d87c775e9082b135e1c4c714a61eafbcf5d6f4cf911"


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

def getthinkpad_offer(offer_id='5624261474'):
    headers = {'content-type': 'application/json'}
    t = requests.get(
            'http://api.natelefon.pl/v1/allegro/offers/%s?access_token=93f25f292141e6824da2a235edcf59292d69febaa06d0798e80905ba440201b6' % offer_id,
            headers=headers
    )
    return t



