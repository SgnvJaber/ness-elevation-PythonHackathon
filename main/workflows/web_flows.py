import time

import allure
from selenium.webdriver import ActionChains
from smart_assertions import soft_assert, verify_expectations
import configuration.conftest
from main import utilities
from main.extensions import verifications
from main.extensions.db_actions import DB_Actions
from main.extensions.ui_actions import Ui_Actions
from main.utilities import base


class Web_Flows():

    @staticmethod
    @allure.step("Sign in Flow:")
    def action_sign_in(username, password):
        Ui_Actions.update_text(base.login_page.get_username_field(), username)
        Ui_Actions.update_text(base.login_page.get_password_field(), password)
        Ui_Actions.click(base.login_page.submit())

    @staticmethod
    @allure.step("sign up new users + verify existence")
    def action_sign_up_new_users():
        list_of_users = DB_Actions.get_list_of_new_users()
        for new_user in list_of_users:
            Web_Flows.add_new_user(new_user)
            Web_Flows.verify_new_user_added(new_user)
            if len(base.get_started_form_page.get_list_of_forms()) > 0:
                Web_Flows.fill_get_started_form(new_user)
            Web_Flows.action_log_out()


    @staticmethod
    @allure.step("log out")
    def action_log_out():
        Ui_Actions.click(base.menu_page.get_logout_btn())

    @staticmethod
    @allure.step("signup new user")
    def add_new_user(new_user):
        Ui_Actions.elem_double_click(base.login_page.get_signup_link())
        Ui_Actions.update_text(base.signup_page.get_firstName_field(), new_user[0])
        Ui_Actions.update_text(base.signup_page.get_lastName_field(), new_user[1])
        Ui_Actions.update_text(base.signup_page.get_username_field(), new_user[2])
        Ui_Actions.update_text(base.signup_page.get_password_field(), new_user[3])
        Ui_Actions.update_text(base.signup_page.get_confirmPassword_field(), new_user[3])
        Ui_Actions.click(base.signup_page.get_submit_btn())

    @staticmethod
    @allure.step("signup new user")
    def verify_new_user_added(new_user):
        Web_Flows.action_sign_in(new_user[2], new_user[3])
        verifications.do_soft_assert(new_user[2], base.menu_page.get_username_logged_in().text.split('@')[1])

    @staticmethod
    @allure.step("signup new user")
    def fill_get_started_form(new_user):
        Ui_Actions.click(base.get_started_form_page.get_first_page_next_btn())
        Ui_Actions.update_text(base.get_started_form_page.get_bank_name_input(), new_user[4])
        Ui_Actions.update_text(base.get_started_form_page.get_routing_number_input(), new_user[5])
        Ui_Actions.update_text(base.get_started_form_page.get_account_number_input(), new_user[6])
        Ui_Actions.click(base.get_started_form_page.get_save_data_btn())
        Ui_Actions.click(base.get_started_form_page.get_done_btn())

    @staticmethod
    @allure.step("make a transaction")
    def make_transaction(contact_name, amount_to_transact, transaction_note):
        Ui_Actions.click(base.navbar_page.get_new_transaction())
        Ui_Actions.update_text(base.transaction_page.get_search_input(), contact_name)
        Ui_Actions.click(base.transaction_page.get_contact_person())
        Ui_Actions.update_text(base.transaction_page.get_amount_input(), amount_to_transact)
        Ui_Actions.update_text(base.transaction_page.get_note_input(), transaction_note)
        current_balance = base.menu_page.get_balance().text.split('$')[1]
        Ui_Actions.click(base.transaction_page.get_payment_submit())
        time.sleep(5)
        return current_balance

    @staticmethod
    @allure.step("get a menus size")
    def get_menus_size():
       return len(base.menu_page.get_menus_size())







