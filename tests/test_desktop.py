import allure
import pytest
from configuration.conftest import *
from main.extensions import verifications
from main.extensions.db_actions import DB_Actions
from main.workflows.desktop_flows import Desktop_Flows


@pytest.mark.usefixtures('init_desktop')
class Test_Desktop:
    key_value = "first_input,operator,second_input,expected"
    my_list = [("3", "+", "5", "8"), ("3", "-", "5", "-2"), ("3", "*", "5", "15")]
    lis = base.my_calculation

    def teardown_method(cls):
        Desktop_Flows.action_clear_display()

    @allure.title("Verify Operations")
    @allure.step("This test verify that the calculator add operation works as expected")
    @pytest.mark.parametrize(key_value, my_list)
    def test__verify_add_operation(self, first_input, operator, second_input, expected):
        Desktop_Flows.operation(first_input, operator, second_input)
        expected_result = float(expected)
        calc_result = Desktop_Flows.action_get_operation_result()
        verifications.verify_equals(expected_result, calc_result)
