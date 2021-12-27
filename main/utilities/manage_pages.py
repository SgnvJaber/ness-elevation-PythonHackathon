from main.pageObjects.real_world.get_started_form_page import Get_Started_Form_Page
from main.pageObjects.real_world.menu_page import Menu_Page
from main.pageObjects.real_world.login_page import Login_Page
from main.pageObjects.real_world.signup_page import Signup_Page
from main.utilities import base

login_page = None


class Manage_Pages:
    @staticmethod
    def init_web_pages(driver):
        base.login_page = Login_Page(driver)
        base.signup_page = Signup_Page(driver)
        base.menu_page = Menu_Page(driver)
        base.get_started_form_page = Get_Started_Form_Page(driver)


