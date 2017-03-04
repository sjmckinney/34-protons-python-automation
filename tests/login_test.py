# filename tests/login_test.py

import pytest
from pages import login_page


class TestLogin:

    USER = "user"
    VALID_PWD = "123"
    INVALID_PWD = "321"

    @pytest.fixture
    def login(self, driver):
        return login_page.LoginPage(driver)

    def test_displays_page_loading_with_valid_credentials(self, login):
        login.with_(self.USER, self.VALID_PWD)
        assert login.loading_message()

    def test_main_page_loads(self, login):
        mainpage = login.with_(self.USER, self.VALID_PWD)
        assert mainpage.page_loaded()
