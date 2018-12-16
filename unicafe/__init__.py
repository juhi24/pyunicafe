# coding: utf-8
import datetime

import requests

API_URL = 'http://messi.hyyravintolat.fi/publicapi'


def parse_date(date_str):
    """Parse API date string as datetime.date."""
    day_str = date_str.split(' ')[1]
    day, month = map(int, day_str.split('.'))
    return datetime.date(datetime.date.today().year, month, day)


def restaurants():
    """Query API for the list of restaurants."""
    url = API_URL + '/restaurants'
    return requests.get(url).json()


def restaurant(rid):
    """Query API for a restaurant by id."""
    url = API_URL + '/restaurant/{}'.format(rid)
    return requests.get(url).json()

