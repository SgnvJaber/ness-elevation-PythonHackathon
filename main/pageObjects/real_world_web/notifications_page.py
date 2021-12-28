import allure
from selenium.webdriver.common.by import By


class Notifications_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get List of Dismiss Button Elements")
    def get_dismiss_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[class='MuiListItem-root MuiListItem-gutters'] > button")
