import configuration
from configuration.conftest import *
from main.extensions.db_actions import DB_Actions
from main.utilities.common_ops import Common_Ops
from main.workflows.web_flows import Web_Flows


@pytest.mark.usefixtures('init_web_app')
class Test_Real_World_Web:
    def test_verify_login(self):
        Web_Flows.action_sign_in(Common_Ops.get_data("username"), Common_Ops.get_data("password"))

    def test_verifyX(self):
        print("Hello")
        print(configuration.conftest.mydb)
        DB_Actions.get_list_of_new_users(configuration.conftest.mydb)
        print(DB_Actions.get_list_of_new_users(configuration.conftest.mydb))