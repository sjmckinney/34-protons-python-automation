# filename: pages/main_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    browser_title = "Demo page for selenium code"
    _main_page_title = {"by": By.ID, "value": "title"}


    def __init__(self, driver, bypass_login=False):
        self.driver = driver
        if bypass_login:
            self._visit("/login.php")

    def page_loaded(self):
        return self.wait_for_title_to_be(self.browser_title)
