from pages.base_page import BasePage
from .locators import LandingPageElements


class LandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LandingPageElements

    def click_region_menu(self):
        ele = self._find_element_info(self.locators.region_menu_ele)
        self._click_element(ele)

    def check_region_menuitem_display(self):
        ele = self._find_element_info(self.locators.region_menu_item_ele)
        return self._check_element_display(ele)

    def check_region_menu_close_btn_display(self):
        ele = self._find_element_info(self.locators.region_menu_close_btn_ele)
        return self._check_element_display(ele)

    def click_region_menu_close_btn(self):
        ele = self._find_element_info(self.locators.region_menu_close_btn_ele)
        self._click_element(ele)

    def click_region_item(self, region_name):
        region_name_tuple = (region_name, )
        origin_region_name_ele = self.locators.region_name_ele
        self.locators.region_name_ele += region_name_tuple
        ele = self._find_element_info(self.locators.region_name_ele)
        self.locators.region_name_ele = origin_region_name_ele
        self._click_element(ele)

    def check_login_btn_display(self):
        ele = self._find_element_info(self.locators.login_btn_ele)
        return self._check_element_display(ele)

    def check_landing_page_load(self):
        self._check_webpage_load_complete()
