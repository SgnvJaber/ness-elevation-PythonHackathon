import allure
from selenium.webdriver.common.by import By


class Fn_Main_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get List of items")
    def get_list_of_items(self):
        return self.driver.find_elements(By.XPATH, "//*[@id='mainGrid']/*/*[@id='text']")

    @allure.step("Get List of items")
    def get_title_element(self):
        return self.driver.find_element(By.XPATH, "//*[@id='toolbar']/android.widget.TextView")

    @allure.step("Get Calculator Element ")
    def get_calculator_element(self):
        return self.driver.find_element(By.XPATH, "//*[@text='Calculator']")

