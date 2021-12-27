import allure
from selenium.webdriver.common.by import By


class Fn_Calculator_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get Amount field")
    def get_number_field(self, number):
        xpath = "//*[@id='digit_" + str(number) + "']"
        return self.driver.find_element(By.XPATH, xpath)

    @allure.step("Get Equal Button")
    def get_equal_button_element(self):
        return self.driver.find_element(By.XPATH, "//*[@id='eq']")

    @allure.step("Get Mult Button")
    def get_add_button_element(self):
        return self.driver.find_element(By.XPATH, "//*[@id='op_add']")

    @allure.step("Get Add Button")
    def get_mult_button_element(self):
        return self.driver.find_element(By.XPATH, "//*[@id='op_mul']")

    @allure.step("Get Result")
    def get_result_element(self):
        return self.driver.find_element(By.XPATH, "//*[@id='formula']")

    @allure.step("Multiply Operation")
    def action_get_multiply_result(self, first_input, second_input):
        self.get_number_field(first_input).click()
        self.get_mult_button_element().click()
        self.get_number_field(second_input).click()
        self.get_equal_button_element().click()
        return self.get_result_element().text

    @allure.step("Add Operation")
    def action_get_add_result(self, first_input, second_input):
        self.get_number_field(first_input).click()
        self.get_add_button_element().click()
        self.get_number_field(second_input).click()
        self.get_equal_button_element().click()
        return self.get_result_element().text
