import allure
import requests

from main.utilities import base


class Api_Actions:

    @staticmethod
    @allure.step('Post new data to server.')
    def post_to_server(category_name, payload):
        return requests.post(base.server_url + category_name, json=payload, headers=base.header).status_code

    @staticmethod
    @allure.step('Get data from server based category.')
    def get_from_server(category):
        return requests.get(base.server_url + category)

    @staticmethod
    @allure.step('Update data patialy.')
    def patch_data(category, item_id, payload):
        return requests.patch(base.server_url + category + "/" + str(item_id), json=payload).status_code
