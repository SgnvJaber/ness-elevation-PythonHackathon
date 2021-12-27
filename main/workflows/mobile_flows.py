import allure

from main.extensions.ui_actions import Ui_Actions
from main.utilities import base


class Mobile_Flows:

    @staticmethod
    @allure.step("Get List Size")
    def action_get_list_size():
        return len(base.fn_main.get_list_of_items())

    @staticmethod
    @allure.step("Get App Title")
    def action_get_app_title():
        return Ui_Actions.get_text(base.fn_main.get_title_element())

    @staticmethod
    @allure.step("Navigate to Calculator")
    def action_get_navigate_to_calculator():
        Ui_Actions.click(base.fn_main.get_calculator_element())

    @staticmethod
    @allure.step("Multiply Operation")
    def action_get_multiply_result(first_input, second_input):
        Ui_Actions.click(base.fn_calculator.get_number_field(first_input))
        Ui_Actions.click(base.fn_calculator.get_mult_button_element())
        Ui_Actions.click(base.fn_calculator.get_number_field(second_input))
        Ui_Actions.click(base.fn_calculator.get_equal_button_element())
        return Ui_Actions.get_text(base.fn_calculator.get_result_element())

    @staticmethod
    @allure.step("Add Operation")
    def action_get_add_result(first_input, second_input):
        Ui_Actions.click(base.fn_calculator.get_number_field(first_input))
        Ui_Actions.click(base.fn_calculator.get_add_button_element())
        Ui_Actions.click(base.fn_calculator.get_number_field(second_input))
        Ui_Actions.click(base.fn_calculator.get_equal_button_element())
        return Ui_Actions.get_text(base.fn_calculator.get_result_element())
