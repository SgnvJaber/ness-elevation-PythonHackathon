import allure


class DB_Actions:

    @staticmethod
    @allure.step("Return list of users from DB")
    def get_list_of_new_users(mydb):
        query = "SELECT * FROM RWANewUsers"
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        my_result = my_cursor.fetchall()
        return my_result
