import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=__option_setting())
    yield driver
    driver.quit()

def __option_setting():
    options = webdriver.ChromeOptions()
    options.browser_version = "stable"
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    return options
