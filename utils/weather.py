import os
import requests


def get_weather(lat, lon, req_type='daily', duration=1):
    if(
            (req_type == 'daily' and duration in [1, 5, 10])
            or (req_type == 'hourly' and duration in [1, 12, 24])
    ):
        url = 'https://atlas.microsoft.com/weather/forecast/{}/json'.format(req_type)
        params = {
            'api-version': '1.0',
            'subscription-key': os.environ["AZURE_MAP_KEY"],
            'categorySet': '9357',
            'query': '{},{}'.format(lat, lon),
            'duration': str(duration),
        }
        return requests.get(url, params)
    else:
        return "Invalid Selection"
