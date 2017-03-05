# filename tests/login_test.py

import pytest
from pages import main_page


class TestMainPage:

    @pytest.fixture
    def mainpage(self, driver):
        return main_page.MainPage(driver, True)

    def test_mainpage_displays_correct_title(self, mainpage):
        assert mainpage.page_loaded()
