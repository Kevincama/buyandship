import time

import pytest

from pages import LandingPage
from config.config import URLConfig
from testdata import load_test_data


class TestLandingPage:
    TEST_URL = URLConfig.LANDING_PAGE_URL.value

    @pytest.fixture(autouse=True)
    def setup(self, browser_driver):
        self.browser_driver = browser_driver
        self.browser_driver.get(self.TEST_URL)
        self.landing_page = LandingPage(browser_driver)

    @pytest.mark.parametrize('load_test_data', ['landing_page.json'], indirect=True)
    def test_switch_region_from_landing_page(self, load_test_data):
        # 以台灣網站為出發點，切換至所有國家
        count = 0

        testdata_region_names = load_test_data['Switch_Region']['Expect_result']['names']
        testdata_region_urls = load_test_data['Switch_Region']['Expect_result']['urls']
        # 第一次載入的頁面不需要測試切換
        testdata_region_names.pop(testdata_region_urls.index(self.TEST_URL))
        testdata_region_urls.remove(self.TEST_URL)
        test_count = len(load_test_data['Switch_Region']['Expect_result']['urls'])

        while count != test_count:
            if not self.landing_page.check_login_btn_display():
                pytest.fail(f"原始網頁{self.TEST_URL}顯示異常，登入按鈕沒顯示")
            self.landing_page.check_landing_page_load()

            self.landing_page.click_region_menu()
            self.landing_page.check_region_menuitem_display()
            if not self.landing_page.check_region_menuitem_display():
                pytest.fail(f"地區選單元件沒顯示")

            self.landing_page.click_region_item(testdata_region_names[count])
            if not self.landing_page.check_login_btn_display():
                pytest.fail(f"該地區{testdata_region_names}：網頁顯示異常，登入按鈕沒顯示")
            self.landing_page.check_landing_page_load()

            assert self.browser_driver.current_url in testdata_region_urls, f"該URL不存在於TestData，請新增或確認正確性"
            time.sleep(3)
            self.browser_driver.back()

            # 有的時候Back回上一頁，地區選單還繼續顯示，故作此判斷
            if self.landing_page.check_region_menu_close_btn_display():
                self.landing_page.click_region_menu_close_btn()
            count += 1
