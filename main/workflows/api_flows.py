import json

import allure
import requests

from main.extensions.api_actions import Api_Actions
from main.utilities import base


class Api_Flows:

    @staticmethod
    @allure.step('Add new song to server')
    def add_new_song(author, song_title, year):
        payload = {'author': author, 'song-title': song_title, 'year': year}
        return Api_Actions.post_to_server("songs", payload)

    @staticmethod
    @allure.step('Get data from server based category')
    def get_data_based_category(category):
        response = Api_Actions.get_from_server(category)
        pretty_json = json.loads(response.text)
        print(json.dumps(pretty_json, indent=2))
        return response.status_code

    @staticmethod
    @allure.step('Update partial data in server data base.')
    def patch_songs_data(category, item_id, author_name, song_name):
        payload = {'author': author_name, 'song-title': song_name}
        return Api_Actions.patch_data(category, item_id, payload)
