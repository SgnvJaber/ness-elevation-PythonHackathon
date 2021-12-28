import allure
from selenium.webdriver.common.by import By


class Login_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get Username field Element")
    def get_username_field(self):
        return self.driver.find_element(By.ID, "username")

    @allure.step("Get Password field Element")
    def get_password_field(self):
        return self.driver.find_element(By.ID, "password")

    @allure.step("Get submit Button")
    def submit(self):
        return self.driver.find_element(By.XPATH, "//button[@data-test='signin-submit']")

    @allure.step("Get goto submit page")
    def get_signup_link(self):
        return self.driver.find_element(By.XPATH, "//a[@data-test='signup']")
