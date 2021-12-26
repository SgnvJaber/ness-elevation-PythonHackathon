from main.pageObjects.real_world.login_page import Login_Page

login_page = None


class Manage_Pages:
    @staticmethod
    def init_web_pages(driver):
        globals()["login_page"] = Login_Page(driver)
