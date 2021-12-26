import mysql.connector
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from configuration.edge_driver_fix import EdgeChromiumDriverManager
from main.utilities.common_ops import Common_Ops
from main.utilities.manage_pages import Manage_Pages

# global driver
# global mydb
driver = None
mydb = None

@pytest.fixture(scope='class')
def init_web_app(request):
    init_driver(request)
    Manage_Pages.init_web_pages(driver)
    globals()["mydb"] = init_DB()
    request.cls.mydb = globals()["mydb"]
    yield
    mydb.close()
    driver.quit()


def init_DB():
    mydb = mysql.connector.connect(
        host=Common_Ops.get_data("host"),
        database=Common_Ops.get_data("databaseDB"),
        user=Common_Ops.get_data("usernameDB"),
        password=Common_Ops.get_data("passwordDB")
    )
    return mydb


def init_driver(request):
    if Common_Ops.get_data("Browser") == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif Common_Ops.get_data("Browser") == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif Common_Ops.get_data("Browser") == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise Exception("Invalid Browser Type")
    globals()["driver"] = driver
    driver.get("http://localhost:4000/")
    # request.cls.driver = driver
