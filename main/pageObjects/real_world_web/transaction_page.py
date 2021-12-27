import allure
from selenium.webdriver.common.by import By


class Transaction_Page:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get search input")
    def get_search_input(self):
        return self.driver.find_element(By.ID, "user-list-search-input")

    @allure.step("Get contact person")
    def get_contact_person(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-test='users-list']")

    @allure.step("Get amount input")
    def get_amount_input(self):
        return self.driver.find_element(By.ID, "amount")

    @allure.step("Get note input")
    def get_note_input(self):
        return self.driver.find_element(By.ID, "transaction-create-description-input")

    @allure.step("Get submit payment")
    def get_payment_submit(self):
        return self.driver.find_element(By.XPATH, '//*[@data-test="transaction-create-submit-payment"]')


