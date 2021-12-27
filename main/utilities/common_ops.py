import csv
import xml.etree.ElementTree as ET


class Common_Ops:
    @staticmethod
    def get_data(node_name):
        root = ET.parse('..\configuration\configuration.xml').getroot()
        return root.find(".//" + node_name).text

    @staticmethod
    def replace_comma(num):
        if ',' in num:
            return num.replace(',', '')
        return num

    @staticmethod
    def get_data_from_csv():
        my_list = []
        with open('..\ddt_files\calculation.csv', newline='') as f:
            reader = csv.reader(f)
            my_list = [tuple(row) for row in reader]
            return my_list
