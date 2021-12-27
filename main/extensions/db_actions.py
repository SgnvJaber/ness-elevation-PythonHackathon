import allure

from main.utilities import base


class DB_Actions:

    @staticmethod
    @allure.step("Return list of users from DB")
    def get_list_of_new_users():
        query = "SELECT * FROM RWANewUsers"
        my_cursor = base.my_db.cursor()
        my_cursor.execute(query)
        my_result = my_cursor.fetchall()
        return my_result
    #
    # @staticmethod
    # @allure.step("Return list of users from DB")
    # def get_calculation_data():
    #     query = "SELECT * FROM Calculation"
    #     my_cursor = base.my_db.cursor()
    #     my_cursor.execute(query)
    #     my_result = my_cursor.fetchall()
    #     return my_result
