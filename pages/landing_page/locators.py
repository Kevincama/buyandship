from selenium.webdriver.common.by import By


class LandingPageElements:
    region_menu_ele = (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div')
    region_menu_item_ele = (By.XPATH, '//*[@id="html"]/body/aside/div[2]/div[2]/ul')
    region_menu_close_btn_ele = (By.XPATH, '//*[@id="html"]/body/aside/div[2]/div[1]/button/span')
    region_name_ele = (By.LINK_TEXT, )
    login_btn_ele = (By.XPATH, '//*[@id="bsHeader"]/header/div[2]/a/span')
