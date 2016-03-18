import requests
import json

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

