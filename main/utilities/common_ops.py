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
