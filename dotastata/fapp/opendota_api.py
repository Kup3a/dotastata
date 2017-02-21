# coding: utf-8
import requests

GET_MATCH_URL = 'https://api.opendota.com/api/matches'
GET_MATCH_URL_PARAMS = ('match_id', )

GET_LEAGUES_URL = 'https://api.opendota.com/api/leagues'


def _make_request(url, params=None):
    """
    Make an request to specified opendota api url.

    :param str url: opendota api url
    :param dict params: for opendota api request
    :return: list of leagues
    """
    r = requests.get(url, params=params)
    if r.status_code == 200:
        try:
            return r.json()
        except ValueError:
            return 'Ooops, invalid json'
    else:
        return 'Status = {status}, error message = {message}'.format(status=r.status_code, message=r.text)


def get_opendota_match(match_id):
    return _make_request(GET_MATCH_URL, params={'match_id': match_id})


def get_opendota_league_list():
    return _make_request(GET_LEAGUES_URL)
