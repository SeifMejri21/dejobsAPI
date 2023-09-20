# from django.test import TestCase
from pprint import pprint

import requests as req

BASE = "http://127.0.0.1:8000/"


def companies_list():
    url = BASE + "company"
    resp = req.get(url)
    data = resp.json()
    pprint(data)
    return data


companies_list()
