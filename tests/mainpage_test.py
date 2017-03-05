# filename tests/mainpage_test.py

import pytest
from pages import main_page
import logging
logging.basicConfig(filename="test.log", level=logging.INFO)


class TestMainPage:

    @pytest.fixture
    def mainpage(self, driver):
        """Returns instance of main page by-passing the login page"""
        print("Created instance of main page")
        logging.info("Created instance of main page")
        return main_page.MainPage(driver, True)

    def test_mainpage_displays_correct_title(self, mainpage):
        assert mainpage.page_loaded()
