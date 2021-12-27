import allure
from selenium.webdriver.common.by import By


class NavBar_Page:
    def __init__(self, driver):
        self.driver = driver
    @allure.step("Get new transaction")
    def get_new_transaction(self):
        return self.driver.find_element(By.XPATH, '//*[@data-test="nav-top-new-transaction"]')