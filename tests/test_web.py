import math

import allure

from configuration.conftest import *
from main.extensions import verifications
from main.utilities.common_ops import Common_Ops
from main.workflows.web_flows import Web_Flows


@pytest.mark.usefixtures('init_web_app')
class Test_Web:

    def setup_method(self):
        Web_Flows.sign_in(Common_Ops.get_data("username"), Common_Ops.get_data("password"))

    def teardown_method(self):
        pass
        # Web_Flows.log_out()

    @allure.title("Verify Login")
    @allure.step("this test verify login works")
    def test_verify_login(self):
        actual_balance = base.menu_page.get_balance().text.split('$')[1]
        Web_Flows.log_out()
        verifications.verify_equals(actual_balance, Common_Ops.get_data('expected_balance'))

    @allure.title("Verify Signup")
    @allure.step("this test verify sign up flow succeeds in adding new users")
    def test_signup_new_users(self):
        Web_Flows.log_out()
        Web_Flows.sign_up_new_users()
        verifications.do_verify_expectations()

    @allure.title("Verify Transaction Works as expected")
    @allure.step("this test verify transaction succeeds in transferring money ")
    def test_transaction(self):
        current_balance = Common_Ops.remove_comma(
            Web_Flows.make_transaction(Common_Ops.get_data("contactNameToSearch"),
                                       Common_Ops.get_data("amountToTransact"),
                                       Common_Ops.get_data("transactNote")))
        new_balance = Common_Ops.remove_comma(
            base.menu_page.get_balance().text.split('$')[1])
        Web_Flows.log_out()
        verifications.verify_equals(math.ceil(float(current_balance) - float(new_balance)),
                                    float(Common_Ops.get_data("amountToTransact")))

    @allure.title("Verify Menu Size is as expected")
    @allure.step("this test that menu size is as expected ")
    def test_get_menus_size(self):
        size = Web_Flows.get_menu_size()
        Web_Flows.log_out()
        verifications.verify_equals(size, int(Common_Ops.get_data("menusSize")))

    @allure.title("Verify Notification Change Using Appli tools")
    @allure.step("this test verify notification is removed using automating graphic elements ")
    def test_notification_change_applitools(self):
        Web_Flows.remove_notification("test_really")
        Web_Flows.log_out()
