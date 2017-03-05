# filename tests/login_test.py

import pytest
from pages import login_page
import logging
logging.basicConfig(filename="test.log", level=logging.INFO)


class TestLogin:

    USER = "user"
    VALID_PWD = "123"
    INVALID_PWD = "321"

    @pytest.fixture
    def login(self, driver):
        """Returns instance of login page"""
        print("Created instance of login page")
        logging.info("Created instance of login page")
        return login_page.LoginPage(driver)

    def test_displays_page_loading_message_with_valid_credentials(self, login):
        login.with_(self.USER, self.VALID_PWD)
        assert login.loading_message()

    def test_displays_error_message_with_invalid_credentials(self, login):
        login.with_(self.USER, self.INVALID_PWD)
        assert login.error_message()

    def test_main_page_loads_after_valid_credentials_supplied(self, login):
        mainpage = login.with_(self.USER, self.VALID_PWD)
        assert mainpage.page_loaded()
