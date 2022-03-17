import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout
from datetime import date

# PLEASE PUT CORRECT REFERENCES TO CODE FORMATS COPIED FROM REAL PYTHON
base_url = "https://ergast.com/api/f1"

today = date.today()
current_year = today.year
ergst_earliest_date = date(1950, 1, 1)  # Filling in month=1, day=1 so date obj created
earliest_year = ergst_earliest_date.year

first_rnd = 1
last_rnd = 22


def season_checker(season, keyword=True):

    if keyword:
        if (season == "current"):
            return True
        return False

    elif ((earliest_year < season and season < current_year) and (f"{season}".isdigit())):
        return True
    else:
        return False


def rnd_checker(rnd, keyword=True):

    if keyword:
        if (rnd == "next" or rnd == "last"):
            return True
        return False

    elif ((first_rnd < rnd and rnd < last_rnd) and (f"{rnd}".isdigit())):
        return True
    else:
        return False


def url_builder(season="current", rnd="next"):
    endpoint = f"{base_url}/{season}/{rnd}.json"
    return endpoint


# Maybe don't have this take anyparametes and it just makes a call to url_builder w/in?
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
