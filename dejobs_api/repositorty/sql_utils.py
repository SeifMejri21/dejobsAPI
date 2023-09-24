import psycopg2
from decouple import config

from utils.helpers import sql_to_dict


# def concat_addresses(addresses_list):
#     strin = ''
#     for a in addresses_list:
#         strin += f"'{a}',"
#     return strin[:-1]


class SQLUtils(object):
    @staticmethod
    def set_db_credentials(db='local'):
        if db == 'local':
            DB_NAME = config('LOCAL_DB_NAME')
            DB_USER = config('LOCAL_DB_USER')
            DB_PASSWORD = config('LOCAL_DB_PASSWORD')
            DB_HOST = config('LOCAL_DB_HOST')
            DB_PORT = config('LOCAL_DB_PORT')
        elif db == 'prod':
            DB_NAME = config('PROD_DB_NAME')
            DB_USER = config('PROD_DB_USER')
            DB_PASSWORD = config('PROD_DB_PASSWORD')
            DB_HOST = config('PROD_DB_HOST')
            DB_PORT = config('PROD_DB_PORT')
        else:
            DB_NAME = config('LOCAL_DB_NAME')
            DB_USER = config('LOCAL_DB_USER')
            DB_PASSWORD = config('LOCAL_DB_PASSWORD')
            DB_HOST = config('LOCAL_DB_HOST')
            DB_PORT = config('LOCAL_DB_PORT')
        return DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

    def create_connection_non_ssh(self, db='local'):
        DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT = self.set_db_credentials(db=db)
        try:
            return psycopg2.connect(
                "host=" + DB_HOST + " dbname=" + DB_NAME + " user=" + DB_USER + " password=" + DB_PASSWORD +
                " port=" + DB_PORT)
        except Exception as e:
            print(e)

    def create_connection(self, db='local', ssh=False):
        conn = None
        try:
            if ssh:
                conn = self.create_connection_ssh(db=db)
            else:
                conn = self.create_connection_non_ssh(db=db)
        except Exception as e:
            print('create_connection ERROR ', e)
        return conn

    def execute_query(self, query, db='local', ssh=False):
        try:
            conn = self.create_connection(db=db, ssh=ssh)
            curr = conn.cursor()
            curr.execute(query)
            records = curr.fetchall()
            conn.close()
        except Exception as e:
            records = []
            print("Error", e)
            print("in query: ", query)
        return records

    def execute_non_select(self, query, db='local', ssh=False):
        try:
            conn = self.create_connection(db=db, ssh=ssh)
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            conn.close()
        except Exception as e:
            print("Error", e)
            print("in query: ", query)


class DbDataLoader(object):
    def __init__(self, db):
        self.sql_utils = SQLUtils()
        self.db = db

    def get_available_jobs_count(self, ssh=False):
        query = f"""SELECT count(*)::INTEGER as ct from  jobs;"""
        data = self.sql_utils.execute_query(query=query, db=self.db, ssh=ssh)
        print(data)
        count = data[0][0]
        return {'jobs_count': count}

    def get_available_jobs(self, limit=100, offset=0, ssh=False):
        query = f"""SELECT jobs.title, jobs.location, jobs.apply_url, companies.name, companies.logo,companies.website,
                    companies.symbol FROM jobs, companies  WHERE jobs.company_symbol = companies.symbol
                    Limit {limit} OFFSET {offset};"""
        data = self.sql_utils.execute_query(query=query, db=self.db, ssh=ssh)
        data = sql_to_dict(data, ['title', 'location', 'apply_url', 'company_name', 'company_logo', 'company_website',
                                  'company_symbol'], type=2)
        return data

    def get_all_available_jobs(self, ssh=False):
        query = f"""SELECT jobs.title, jobs.location, jobs.apply_url, companies.name, companies.logo,companies.website,
                    companies.symbol FROM jobs, companies  WHERE jobs.company_symbol = companies.symbol ;"""
        data = self.sql_utils.execute_query(query=query, db=self.db, ssh=ssh)
        data = sql_to_dict(data, ['title', 'location', 'apply_url', 'company_name', 'company_logo', 'company_website',
                                  'company_symbol'], type=2)
        return data

    def get_available_jobs_filtered(self, limit=100, offset=0, ssh=False):
        query = f"""SELECT jobs.title, jobs.location, jobs.apply_url, companies.name, companies.logo,companies.website,
                    companies.symbol FROM jobs, companies  WHERE jobs.company_symbol = companies.symbol
                    Limit {limit} OFFSET {offset};"""
        data = self.sql_utils.execute_query(query=query, db=self.db, ssh=ssh)
        data = sql_to_dict(data, ['title', 'location', 'apply_url', 'company_name', 'company_logo', 'company_website',
                                  'company_symbol'], type=2)
        return data

    def get_jobs_filters(self, ssh=False):
        titles, companies_names, locations = [], [], []
        query = f"""SELECT title, company_name, location FROM jobs;"""
        data = self.sql_utils.execute_query(query=query, db=self.db, ssh=ssh)
        for d in data:
            titles.append(d[0])
            companies_names.append(d[1])
            locations.append(d[2])
        setted_titles = sorted(list(set(titles)))
        setted_companies_names = sorted(list(set(companies_names)))
        setted_locations = sorted(list(set(locations)))
        return {"titles": setted_titles, "companies_names": setted_companies_names, "locations": setted_locations}
