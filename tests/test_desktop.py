import allure
from configuration.conftest import *
from main.extensions import verifications
from main.workflows.desktop_flows import Desktop_Flows


@pytest.mark.usefixtures('init_desktop')
class Test_Desktop:
    key_value = "first_input,operator,second_input,expected"

    def teardown_method(cls):
        Desktop_Flows.clear_display()

    @allure.title("Verify Calculations Operations Using DDT")
    @allure.step("This test verify that the calculator operations works as expected")
    @pytest.mark.parametrize(key_value, Common_Ops.get_data_from_csv())
    def test_verify_operation(self, first_input, operator, second_input, expected):
        Desktop_Flows.operation(first_input, operator, second_input)
        calc_result = Desktop_Flows.get_operation_result()
        verifications.verify_equals(float(expected), calc_result)
