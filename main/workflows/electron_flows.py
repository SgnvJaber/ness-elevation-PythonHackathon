import allure

from main.extensions.ui_actions import Ui_Actions
from main.utilities import base


class Electron_Flows():

    @staticmethod
    @allure.step("Get Menu Size")
    def get_menu_size():
        return Ui_Actions.get_list_size(base.electron_page.get_menu_elements())

    @staticmethod
    @allure.step("Get Communication Button's Attribute")
    def get_communication_attribute():
        Ui_Actions.click(base.electron_page.get_communication_element())
        return Ui_Actions.get_attribute(base.electron_page.get_communication_element(), "class")
