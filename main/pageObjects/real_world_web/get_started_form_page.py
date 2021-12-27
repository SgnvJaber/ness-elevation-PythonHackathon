import allure
from selenium.webdriver.common.by import By


class Get_Started_Form_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get list of forms to verify if the form poped up")
    def get_list_of_forms(self):
        return self.driver.find_elements(By.CLASS_NAME, "MuiDialog-paper")

    @allure.step("First page next btn")
    def get_first_page_next_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-test='user-onboarding-next']")

    @allure.step("Get input of bank name")
    def get_bank_name_input(self):
        return self.driver.find_element(By.ID, "bankaccount-bankName-input")

    @allure.step("Get input of routing number")
    def get_routing_number_input(self):
        return self.driver.find_element(By.ID, "bankaccount-routingNumber-input")

    @allure.step("Get input of account number")
    def get_account_number_input(self):
        return self.driver.find_element(By.ID, "bankaccount-accountNumber-input")


    @allure.step("Save new bank account data button")
    def get_save_data_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-test='bankaccount-submit']")


    @allure.step("Get Done button to finish form")
    def get_done_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-test='user-onboarding-next']")