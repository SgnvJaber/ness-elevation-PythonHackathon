from main.pageObjects.real_world.login_page import Login_Page
from main.utilities import base

login_page = None


class Manage_Pages:
    @staticmethod
    def init_web_pages(driver):
        globals()["login_page"] = Login_Page(driver)
        Login_Page(driver)
        base.login = Login_Page(driver)
