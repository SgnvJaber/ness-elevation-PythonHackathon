import os

import mysql.connector
import pytest
from applitools.selenium import Eyes
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from configuration.edge_driver_fix import EdgeChromiumDriverManager
from main.utilities import base
from main.utilities.common_ops import Common_Ops
from main.utilities.listeners import EventListener
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
    base.driver.quit()


@pytest.fixture(scope='class')
def init_api(request):
    base.server_url = Common_Ops.get_data('serverUrl')
    base.header = {'Content-type': Common_Ops.get_data('contentType')}


@pytest.fixture(scope='class')
def init_desktop(request):
    desired_caps = {}
    desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    desired_caps["platformName"] = "Windows"
    desired_caps["deviceName"] = "WindowsPC"
    edriver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
    base.driver = EventFiringWebDriver(edriver, EventListener())
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
    edriver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    base.driver = EventFiringWebDriver(edriver, EventListener())
    Manage_Pages.init_appium_pages(base.driver)
    yield
    base.driver.quit()


@pytest.fixture(scope='class')
def init_electron(request):
    electron_app = Common_Ops.get_data("elctronApp")
    options = webdriver.ChromeOptions()
    options.binary_location = electron_app
    edriver = Common_Ops.get_data("elctronDriver")
    mdriver = webdriver.Chrome(chrome_options=options, executable_path=edriver)
    driver = EventFiringWebDriver(mdriver, EventListener())
    Manage_Pages.init_electron_pages(driver)
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
    param = Common_Ops.get_data("Browser")
    browser_type = os.getenv('BrowserType')
    # If we got parameter from JENKINS OR CMD use browser type ,else search for browser from XML
    if (browser_type):
        param = browser_type

    if param == "chrome":
        edriver = webdriver.Chrome(ChromeDriverManager().install())
    elif param == "edge":
        edriver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif param == "firefox":
        edriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise Exception("Invalid Browser Type")

    driver = edriver
    # driver = EventFiringWebDriver(edriver, EventListener()) won't work with appli tools
    base.driver = driver
    base.driver.get(Common_Ops.get_data("webUrl"))
