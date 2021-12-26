import time

import allure

import configuration.conftest
from main import utilities
from main.extensions.db_actions import DB_Actions
from main.extensions.ui_actions import Ui_Actions
from main.utilities.manage_pages import login_page


class Web_Flows:

    @staticmethod
    @allure.step("Sign in Flow:")
    def action_sign_in(username, password):
        print(DB_Actions.get_list_of_new_users(configuration.conftest.mydb))
        Ui_Actions.update_text(utilities.manage_pages.login_page.get_username_field(), username)
        Ui_Actions.update_text(utilities.manage_pages.login_page.get_password_field(), password)
        Ui_Actions.click(utilities.manage_pages.login_page.submit())
