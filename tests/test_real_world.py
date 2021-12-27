import configuration
from configuration import conftest
from configuration.conftest import *
from main.extensions import verifications
from main.extensions.db_actions import DB_Actions
from main.utilities.common_ops import Common_Ops
from main.workflows.web_flows import Web_Flows


@pytest.mark.usefixtures('init_web_app')
class Test_Real_World_Web:

    def test_verify_login(self):
        print(conftest.my_action)
        print(self.my_action105)
        print(conftest.my_new_action)
        # Web_Flows.action_sign_in(Common_Ops.get_data("username"), Common_Ops.get_data("password"))
        # actual_balance = base.menu_page.get_balance().text.split('$')[1]
        # Web_Flows.action_log_out()
        # verifications.verify_equals(actual_balance, Common_Ops.get_data('expected_balance'))

    def test_signup_new_users(self):
        Web_Flows.action_sign_up_new_users()
        verifications.do_verify_expectations()
        print()
