import allure
from selenium.webdriver.common.by import By


class Menu_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get balance")
    def get_balance(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-test='sidenav-user-balance']")


    @allure.step("Get logout btn")
    def get_logout_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-test='sidenav-signout']")

    @allure.step("Get username")
    def get_username_logged_in(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-test='sidenav-username']")

    @allure.step("Get menus size")
    def get_menus_size(self):
        return self.driver.find_elements(By.XPATH, "(//*[@class='MuiList-root MuiList-padding'])[1]//a")



