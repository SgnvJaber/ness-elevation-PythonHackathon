from main.pageObjects.calculator_desktop.calculator_page import Calculator_Page
from main.pageObjects.electron_app.electron_main_page import Electron_Main_Page
from main.pageObjects.finan_calculator_appium.fn_calculator_page import Fn_Calculator_Page
from main.pageObjects.finan_calculator_appium.fn_main_page import Fn_Main_Page
from main.pageObjects.real_world_web.get_started_form_page import Get_Started_Form_Page
from main.pageObjects.real_world_web.menu_page import Menu_Page
from main.pageObjects.real_world_web.login_page import Login_Page
from main.pageObjects.real_world_web.nav_bar_page import NavBar_Page
from main.pageObjects.real_world_web.notifications_page import Notifications_Page
from main.pageObjects.real_world_web.signup_page import Signup_Page
from main.pageObjects.real_world_web.transaction_page import Transaction_Page
from main.utilities import base

login_page = None


class Manage_Pages:
    @staticmethod
    def init_web_pages(driver):
        base.login_page = Login_Page(driver)
        base.signup_page = Signup_Page(driver)
        base.menu_page = Menu_Page(driver)
        base.get_started_form_page = Get_Started_Form_Page(driver)
        base.navbar_page = NavBar_Page(driver)
        base.transaction_page = Transaction_Page(driver)
        base.notification_page = Notifications_Page(driver)

    @staticmethod
    def init_desktop_pages(driver):
        base.desktop_calc = Calculator_Page(driver)

    @staticmethod
    def init_appium_pages(driver):
        base.fn_main = Fn_Main_Page(driver)
        base.fn_calculator = Fn_Calculator_Page(driver)

    @staticmethod
    def init_electron_pages(driver):
        base.electron_page = Electron_Main_Page(driver)
