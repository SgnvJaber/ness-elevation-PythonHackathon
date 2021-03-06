import time

import allure

from main.utilities import base


class Ui_Actions:

    @staticmethod
    @allure.step("Click on element")
    def click(element):
        element.click()

    @staticmethod
    @allure.step("Double click on element")
    def elem_double_click(element):
        element.click()
        element.click()

    @staticmethod
    @allure.step("Update element text")
    def update_text(element, text):
        element.send_keys(text)

    @staticmethod
    @allure.step("Get text from element")
    def get_text(element):
        return element.text

    @staticmethod
    @allure.step("Get Element Attribute's value")
    def get_attribute(element, attribute):
        return element.get_attribute(attribute)

    @staticmethod
    @allure.step("Get list size")
    def get_list_size(list):
        return len(list)
