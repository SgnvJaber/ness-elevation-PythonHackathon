import allure


class Ui_Actions:

    @staticmethod
    @allure.step("Click on element")
    def click(element):
        element.click()

    @staticmethod
    @allure.step("Update element text")
    def update_text(element, text):
        element.send_keys(text)
