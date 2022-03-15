import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout
# PLEASE PUT CORRECT REFERENCES TO CODE FORMATS COPIED FROM REAL PYTHON
base_url = "https://ergast.com/api/f1"


def url_builder(season="current", rnd="next"):
    endpoint = f"{base_url}/{season}/{rnd}.json"
    return endpoint


def make_request(endpoint):
    try:
        r = requests.get(endpoint, timeout=5)

        # If the response was succesful, no Exception will be raised
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'Http error occured: {http_err}')
    except ConnectionError as conct_err:
        print(f'Connection Error occured: {conct_err}')
    except Timeout as tout_err:
        print(f'Timeout Error occured: {tout_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')


if ('__name__' == '__main__'):
    pass
