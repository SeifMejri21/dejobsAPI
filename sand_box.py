# from django.test import TestCase

import requests as req

from utils.helpers import read_json


class DeJobsApiTester(object):
    def __init__(self, test_env="local"):
        """
        test_env: (str), 'local' or 'prod'
        """
        self.test_env = test_env
        self.local_base = "http://127.0.0.1:8000/"
        self.prod_base = "https://dejobs-backend.onrender.com/"

    @staticmethod
    def request_builder(request_type, url, data={}):
        if request_type in ["GET", "get", "Get"]:
            resp = req.get(url)
            if resp.status_code == 200:
                data = resp.json()
            else:
                data = 200
                print(f"'GET' request ERROR: {resp.status_code} on  {url}")
        elif request_type in ["POST", "post", "Post"]:
            resp = req.post(url, json=data)
            if resp.status_code != 200:
                print(f"'POST' request ERROR: {resp.status_code} on  {url}")
        return data

    def import_companies_list(self):
        if self.test_env == "prod":
            url = self.local_base + "companies"
        elif self.test_env == "local":
            url = self.prod_base + "companies"
        else:
            url = self.local_base + "companies"
        companies_list = self.request_builder("GET", url)
        return companies_list

    def export_single_company(self, company_info):
        if self.test_env == "prod":
            url = self.local_base + "companies"
        elif self.test_env == "local":
            url = self.prod_base + "companies"
        else:
            url = self.local_base + "companies"
        self.request_builder("POST", url, data=company_info)

    def export_companies_list(self, companies_list):
        for c in companies_list:
            self.export_single_company(c)


firms_info = read_json("firms_info", local=True)
from pprint import pprint

print("len(firms_info): ", len(firms_info))
dat = DeJobsApiTester(test_env="prod")
# dat.export_companies_list(companies_list=firms_info)
# dat.export_companies_list(firms_info)

# for f in firms_info[:10]:
#     # pprint(f)
#     dat.export_companies_list(companies_list=f)
#     print("******************************************************************************************************")


print(
    "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
print(
    "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
print(
    "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
companies_list = dat.import_companies_list()
pprint(companies_list[:5])
print("len(companies_list): ", len(companies_list))

from time import sleep

# i = 0
# for f in firms_info:
#     dat.export_single_company(f)
#     # companies_list = dat.import_companies_list()
#     i += 1
#     print(f"number companies exported {i}, number of companies in db: {len(companies_list)}")
#     # sleep(1)

# for c in companies_list:
#     pprint(c)
#     print("******************************************************************************************************")

# for f in firms_info:
#     pprint(f)
#     print("******************************************************************************************************")
