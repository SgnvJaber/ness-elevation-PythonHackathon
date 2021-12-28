import allure
from selenium.webdriver.common.by import By


class Electron_Main_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get List of menu elements")
    def get_menu_elements(self):
        return self.driver.find_elements(By.XPATH, "//nav/div/h5")

    @allure.step("Get Communication Button element")
    def get_communication_element(self):
        return self.driver.find_element(By.XPATH, "//div[@class='nav-item u-category-communication']/button")
