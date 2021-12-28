import mysql.connector
import pytest
from applitools.selenium import Eyes
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from configuration.edge_driver_fix import EdgeChromiumDriverManager
from main.utilities import base
from main.utilities.common_ops import Common_Ops
from main.utilities.manage_pages import Manage_Pages


@pytest.fixture(scope='class')
def init_web_app(request):
    init_driver(request)
    Manage_Pages.init_web_pages(base.driver)
    base.action = ActionChains(base.driver)
    base.my_db = init_DB()
    base.driver.implicitly_wait(5)
    base.eyes = Eyes()
    base.eyes.api_key = Common_Ops.get_data("appliToolsKey")
    yield
    base.my_db.close()
    # base.driver.quit()


@pytest.fixture(scope='class')
def init_api(request):
    base.server_url = Common_Ops.get_data('serverUrl')
    base.header = {'Content-type': Common_Ops.get_data('contentType')}
    print(base.header, "*******************************")


@pytest.fixture(scope='class')
def init_desktop(request):
    desired_caps = {}
    desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    desired_caps["platformName"] = "Windows"
    desired_caps["deviceName"] = "WindowsPC"
    base.driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
    Manage_Pages.init_desktop_pages(base.driver)
    base.driver.implicitly_wait(5)
    yield
    base.driver.quit()


@pytest.fixture(scope='class')
def init_appium(request):
    desired_caps = {}
    desired_caps['udid'] = 'ce051605b5d4d82c03'
    desired_caps['appPackage'] = 'com.financial.calculator'
    desired_caps['appActivity'] = '.FinancialCalculators'
    desired_caps['platformName'] = 'android'
    base.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    Manage_Pages.init_appium_pages(base.driver)
    yield
    base.driver.quit()


@pytest.fixture(scope='class')
def init_electron(request):
    electron_app = Common_Ops.get_data("elctronApp")
    options = webdriver.ChromeOptions()
    options.binary_location = electron_app
    edriver = Common_Ops.get_data("elctronDriver")
    driver = webdriver.Chrome(chrome_options=options, executable_path=edriver)
    Manage_Pages.init_electron_pages(driver)
    # expected_menu_size = 6
    driver.implicitly_wait(5)
    yield
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
    base.driver = driver
    base.driver.get(Common_Ops.get_data("webUrl"))
