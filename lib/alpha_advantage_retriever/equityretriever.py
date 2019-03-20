import sys, urllib3, datetime, json, re
from apikey.apikey import API_KEY_ALPHA, SECRET_KEY_IEX

# IEX
BASE_URL_IEX = 'https://cloud.iexapis.com/'
SANDBOX_BASE_URL_IEX = 'https://sandbox.iexapis.com'

# ALPHAVANTAGE
BASE_URL_ALPHA = 'https://www.alphavantage.co/'


class QueryError(Exception):
    def __init__(self, value):
        self.value = value


def query_string_alpha(**kwargs):
    query = 'query?'
    for key, value in kwargs.items():
        query = query + str(key) + "=" + str(value) + '&'
    query = query + '&apikey=' + API_KEY_ALPHA
    return query


def query_string_IEX(**kwargs):
    query = 'query?'
    for key, value in kwargs.items():
        query = query + str(key) + "=" + str(value) + '&'
    query = query + '&apikey=' + API_KEY_ALPHA
    return query


def __validate_data(data):
    if 'Error' in data:
        raise QueryError('Query failed with error: "%s".' % data['Error Message'])
    else:
        return data


# for external
def execute_query_alpha(**kwargs):
    http = urllib3.PoolManager()
    response = http.request('GET', BASE_URL_ALPHA + query_string_alpha(**kwargs))
    response_decode = response.data.decode('UTF-8')
    response_decode = re.sub(r"[0-9][0-9]\.\s", "", response_decode)    # clean all 01. stuff
    data = json.loads(response_decode)
    return __validate_data(data)
