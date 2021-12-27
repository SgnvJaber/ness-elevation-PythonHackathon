import allure
from selenium.webdriver.common.by import By


class Calculator_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get Given Number Element")
    def get_number_element(self, number_str):
        xpath = "//*[@AutomationId='num" + number_str + "Button']"
        return self.driver.find_element(By.XPATH, xpath)

    @allure.step("Get Equal element")
    def get_equal_element(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='equalButton']")

    @allure.step("Get Clear element")
    def get_clear_element(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='clearButton']")

    @allure.step("Get Result element")
    def get_result_element(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='CalculatorResults']")

    @allure.step("get operation element")
    def get_operation_element(self, operation):
        xpath = "//*[@AutomationId='" + operation + "Button']"
        return self.driver.find_element(By.XPATH, xpath)

    @allure.step("Convert give Operator to Calculator text")
    def convert_operation_to_calculator(self, operation):
        op_calculator = "plus"
        if (operation == "-"):
            op_calculator = "minus"
        elif (operation == "/"):
            op_calculator = "divide"
        elif (operation == "*"):
            op_calculator = "multiply"
        return op_calculator
