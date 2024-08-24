import pytest
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import DEFAULT_TIMEOUT

# 避免此Class function被直接於test層級呼叫，故加上 _ 作為提醒不應直接使用
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _find_element_info(self, locator_info: str, timeout=DEFAULT_TIMEOUT):
        try:
            return (WebDriverWait(driver=self.driver, timeout=timeout).
                    until(EC.presence_of_element_located(locator=(locator_info[0], locator_info[1])))
                    )
        except Exception as e:
            pytest.fail(f"Element not existed: {e}")

    def _find_elements_info(self, locator_info: str, timeout=DEFAULT_TIMEOUT):
        try:
            return (WebDriverWait(driver=self.driver, timeout=timeout).
                    until(EC.presence_of_all_elements_located(locator=(locator_info[0], locator_info[1])))
                    )
        except Exception as e:
            pytest.fail(f"Elements not existed: {e}")

    def _click_element(self, element: WebElement):
        try:
            element.click()
        except Exception as e:
            pytest.fail(f"Click element fail, element: {element}, Exception: {e}")

    def _check_element_display(self, element: WebElement):
        try:
            return element.is_displayed()
        except Exception as e:
            pytest.fail(f"Element is not display, element: {element}, Exception: {e}")

    def _check_webpage_load_complete(self):
        try:
            if not self.driver.execute_script('return document.readyState') == 'complete':
                pytest.fail(f"WebPage not load complete")
        except Exception as e:
            pytest.fail(f"WebPage not load complete, maybe over timeout, Exception: {e}")

