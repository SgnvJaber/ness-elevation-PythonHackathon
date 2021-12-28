import allure
from main.utilities import base


class DB_Actions:

    @staticmethod
    @allure.step("Return list of users from DB")
    def get_list_of_new_users():
        query = "SELECT * FROM RWANewUsers"
        my_cursor = base.my_db.cursor()
        my_cursor.execute(query)
        results = my_cursor.fetchall()
        return results
