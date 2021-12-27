import time
import allure
from main.extensions.ui_actions import Ui_Actions
from main.utilities import base


class Desktop_Flows():

    @staticmethod
    @allure.step("Calculator Operation on a given input")
    def operation(first_input, operation, second_input):
        if (operation == "/" and second_input == "0"):
            print("Cannot divide number by zero!")
            return
        operator = base.desktop_calc.convert_operation_to_calculator(operation)
        Ui_Actions.click(base.desktop_calc.get_number_element(first_input))
        Ui_Actions.click(base.desktop_calc.get_operation_element(operator))
        Ui_Actions.click(base.desktop_calc.get_number_element(second_input))
        Ui_Actions.click(base.desktop_calc.get_equal_element())
        time.sleep(1)

    @staticmethod
    @allure.step("Get Result")
    def action_get_operation_result():
        result_text = Ui_Actions.get_text(base.desktop_calc.get_result_element()).split("Display is ")[1]
        return float(result_text)

    @staticmethod
    @allure.step("Clear Result")
    def action_clear_display():
        return Ui_Actions.click(base.desktop_calc.get_clear_element())
