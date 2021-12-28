import csv
import xml.etree.ElementTree as ET
import allure


class Common_Ops:

    @staticmethod
    @allure.step("Getting data from external XML file")
    def get_data(node_name):
        root = ET.parse('C:\Automation\Python\python_hackathon\configuration\configuration.xml').getroot()
        return root.find(".//" + node_name).text

    @staticmethod
    @allure.step("Removing comma from number")
    def remove_comma(number):
        if ',' in number:
            return number.replace(',', '')
        return number

    @staticmethod
    @allure.step("Getting external data from CSV file and saving it into a list")
    def get_data_from_csv():
        list = []
        with open(Common_Ops.get_data('CSVFilePath'), newline='') as f:
            reader = csv.reader(f)
            list = [tuple(row) for row in reader]
            return list
