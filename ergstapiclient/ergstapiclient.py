import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout
from datetime import date

base_url = "https://ergast.com/api/f1"

today = date.today()
current_year = today.year
earliest_year = 1950

first_rnd = 1
last_rnd = 22


def season_checker(season, keyword=True):

    if keyword:
        if (season == "current"):
            return True
        return False

    elif ((earliest_year < season and season < current_year) and
          (f"{season}".isdigit())):
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


def is_alpha(endpoint_variable):
   return (f"{endpoint_variable}".isalpha()) 


def correct_format_helper(season, rnd):
    seasonkeyword = is_alpha(season)  
    rndkeyword = is_alpha(rnd)  
    return (season_checker(season, seasonkeyword) and 
            rnd_checker(rnd, rndkeyword))


def url_builder(season="current", rnd="next"):
    endpoint = f"{base_url}/{season}/{rnd}.json"
    return endpoint


def make_request(endpoint):
    """
       The exception format below was borrowed from an article on Real Python
       Link: https://realpython.com/python-requests/
       Title: Python's Requests Library (Guide)
       Article author: Alex Ronquillo
    """

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


if (__name__ == '__main__'):
    pass
