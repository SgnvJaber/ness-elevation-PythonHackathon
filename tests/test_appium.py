import allure

from configuration.conftest import *
from main.extensions import verifications
from main.workflows.mobile_flows import Mobile_Flows

first_num = int(Common_Ops.get_data('firstNum'))
second_num = int(Common_Ops.get_data('secondNumber'))
expected_mult_result = first_num * second_num
expected_add_result = first_num + second_num


@pytest.mark.usefixtures('init_appium')
class Test_Appium:

    @allure.title('Check number of calculator')
    @allure.step('Verify there are 18 calculators')
    def test_number_of_total_calculators(self):
        verifications.verify_equals(Mobile_Flows.get_list_size(), 18)

    @allure.title('Verify app title')
    @allure.step('Verify app title is as expected')
    def test_verify_app_title(self):
        verifications.verify_equals(Mobile_Flows.get_app_title(), Common_Ops.get_data('expectedTitle'))

    @allure.title('Multiply operation')
    @allure.step('Verify result of multiplication is as expected')
    def test_verify_mult_result(self):
        Mobile_Flows.get_navigate_to_calculator()
        result = int(Mobile_Flows.get_multiply_result(first_num, second_num))
        verifications.verify_equals(result, first_num * second_num)
