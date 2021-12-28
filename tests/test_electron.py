import allure

from configuration.conftest import *
from main.extensions import verifications
from main.workflows.electron_flows import Electron_Flows


@pytest.mark.usefixtures('init_electron')
class Test_Electron:

    @allure.title("Verify Menu size is as expected")
    @allure.step("This test verify that the menu size is as expected")
    def test_menu_size(self):
        verifications.verify_equals(Electron_Flows.get_menu_size(), 6)

    @allure.title("Verify Element is Selected")
    @allure.step("This test verify that element is slected after clicking on it")
    def test_element_is_selected(self):
        verifications.contains(Electron_Flows.get_communication_attribute(), "is-selected")
