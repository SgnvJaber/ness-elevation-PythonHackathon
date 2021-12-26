import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import xml.etree.ElementTree as ET

from configuration.edge_driver_fix import EdgeChromiumDriverManager


@pytest.fixture(scope='class')
def init_driver(request):
    if get_data("Browser") == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif get_data("Browser") == "edge":
        srv = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif get_data("Browser") == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver = None
        print("Wrong input, unrecognized browser")
    driver.maximize_window()
    driver.implicitly_wait(1)
    request.cls.driver = driver
    yield
    driver.quit()


def get_data(node_name):
    root = ET.parse('configuration/configuration.xml').getroot()
    return root.find(".//" + node_name).text
