import allure

from configuration.conftest import *
from main.extensions import verifications
from main.workflows.mobile_flows import Mobile_Flows


@pytest.mark.usefixtures('init_appium')
class Test_Fn_Calculator_Appium:

    def test_01(self):
        verifications.verify_equals(Mobile_Flows.action_get_list_size(), 18)

    def test_02_assert_title(self):
        verifications.verify_equals(Mobile_Flows.action_get_app_title(), "fncalculator.com")

    def test_03(self):
        Mobile_Flows.action_get_navigate_to_calculator()
        result = Mobile_Flows.action_get_multiply_result(2, 3)
        verifications.verify_equals(int(result), 2 * 3)

    def test_04(self):
        Mobile_Flows.action_get_navigate_to_calculator()
        result = Mobile_Flows.action_get_add_result(2, 3)
        verifications.verify_equals(int(result), 2 + 3)
