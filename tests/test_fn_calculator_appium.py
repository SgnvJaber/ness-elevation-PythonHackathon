import allure

from configuration.conftest import *


@pytest.mark.usefixtures('init_appium')
class Test_Fn_Calculator_Appium:

    def test_something(self):
        print("Hello world")
