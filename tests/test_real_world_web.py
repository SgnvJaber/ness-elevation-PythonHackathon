import math

from configuration.conftest import *
from main.extensions import verifications
from main.utilities.common_ops import Common_Ops
from main.workflows.web_flows import Web_Flows


@pytest.mark.usefixtures('init_web_app')
class Test_Real_World_Web:

    def test_verify_login(self):
        actual_balance = base.menu_page.get_balance().text.split('$')[1]
        verifications.verify_equals(actual_balance, Common_Ops.get_data('expected_balance'))

    # def test_signup_new_users(self):
    #     Web_Flows.action_log_out()
    #     Web_Flows.action_sign_up_new_users()
    #     verifications.do_verify_expectations()

    # def transication
    # def applitools
    # def menu size
    def test_transaction(self):
        current_balance = Common_Ops.replace_comma(
            Web_Flows.make_transaction(Common_Ops.get_data("contactNameToSearch"),
                                       Common_Ops.get_data("amountToTransact"),
                                       Common_Ops.get_data("transactNote")))
        new_balance = Common_Ops.replace_comma(
            base.menu_page.get_balance().text.split('$')[1])

        print("\n*************************************" + current_balance + " " + new_balance)

        verifications.verify_equals(math.ceil(float(current_balance) - float(new_balance)),
                                    float(Common_Ops.get_data("amountToTransact")))

    def setup_method(self):
        Web_Flows.action_sign_in(Common_Ops.get_data("username"), Common_Ops.get_data("password"))

    def teardown_method(self):
        Web_Flows.action_log_out()

    def test_notification_change_applitools(self):
        Web_Flows.remove_notification("my_test_really")

    def test_get_menus_size(self):
        size = Web_Flows.get_menus_size()
        verifications.verify_equals(size, int(Common_Ops.get_data("menusSize")))
