import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Signup_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get firstName field Element")
    def get_firstName_field(self):
        return self.driver.find_element(By.ID, "firstName")

    @allure.step("Get lastName field Element")
    def get_lastName_field(self):
        return self.driver.find_element(By.ID, "lastName")

    @allure.step("Get username field Element")
    def get_username_field(self):
        return self.driver.find_element(By.ID, "username")

    @allure.step("Get password field Element")
    def get_password_field(self):
        return self.driver.find_element(By.ID, "password")

    @allure.step("Get confirmPassword field Element")
    def get_confirmPassword_field(self):
        return self.driver.find_element(By.ID, "confirmPassword")

    @allure.step("Get submit button")
    def get_submit_btn(self):
        return self.driver.find_element(By.CLASS_NAME, "MuiButton-label")
