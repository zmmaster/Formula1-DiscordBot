import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout
from datetime import date


class UrlBuilder:
    base_url = "https://ergast.com/api/f1"

    today = date.today()
    current_year = today.year
    earliest_year = 1950

    first_rnd = 1
    last_rnd = 22

    @staticmethod
    def season_checker(season, keyword=True):
        if keyword:
            if (season == "current"):
                return True
            return False
        elif ((UrlBuilder.earliest_year < season and
              season < UrlBuilder.current_year) and
              (f"{season}".isdigit())):
            return True
        else:
            return False

    @staticmethod
    def rnd_checker(rnd, keyword=True):

        if keyword:
            if (rnd == "next" or rnd == "last"):
                return True
            return False

        elif ((UrlBuilder.first_rnd < rnd and
              rnd < UrlBuilder.last_rnd) and
              (f"{rnd}".isdigit())):
            return True
        else:
            return False

    @staticmethod
    def is_alpha(endpoint_variable):
        return (f"{endpoint_variable}".isalpha())

    @staticmethod
    def correct_format_helper(season, rnd):
        seasonkeyword = UrlBuilder.is_alpha(season)
        rndkeyword = UrlBuilder.is_alpha(rnd)
        return (UrlBuilder.season_checker(season, seasonkeyword) and
                UrlBuilder.rnd_checker(rnd, rndkeyword))

    def url_builder(season="current", rnd="next"):
        endpoint = f"{UrlBuilder.base_url}/{season}/{rnd}.json"
        return endpoint


class SendRequest:
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
