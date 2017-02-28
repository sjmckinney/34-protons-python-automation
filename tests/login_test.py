# filename tests/login_test.py

import pytest
import os
from selenium import webdriver
from pages import login_page

class TestLogin():

    @pytest.fixture(scope="session")
    def login(self):
        #_geckodriver = os.path.join(os.getcwd(), 'vendor' , 'geckodriver' )
        _geckodriver = "/usr/local/bin/geckodriver"
        driver_ = webdriver.Firefox(executable_path=_geckodriver)
        yield login_page.LoginPage(driver_)
        driver_.quit()


    def test_valid_credentials(self, login):
        login.with_("user", "123")
        assert login.login_success_message()
