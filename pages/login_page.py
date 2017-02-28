# filename: pages/login_page.py

from selenium.webdriver.common.by import By
#from base_page import BasePage
from .base_page import BasePage

class LoginPage(BasePage):
    _login_form = {"by": By.ID, "value": "login"}
    _user_input = {"by": By.ID, "value": "username"}
    _password_input = {"by": By.ID, "value": "password"}
    _submit_button = {"by": By.NAME, "value": "submit"}
    _error_msg = {"by": By.ID, "value": "input_error"}
    _loading_message = {"by": By.ID, "value": "loading"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("http://www.34protons.co.uk/demo_2_0/login.php")
        #self._visit("http://localhost/login.php")
        assert self._is_displayed(self._login_form)

    def with_(self, username, password):
        self._type(self._user_input, username)
        self._type(self._password_input, password)
        self._click(self._submit_button)

    def login_success_message(self):
        if self.wait_for_is_displayed(self._loading_message):
            return self._find(self._loading_message).text == "Loading... Please wait";
