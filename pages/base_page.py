# filename: pages/base_page.py

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests import config
import logging
logging.basicConfig(filename="test.log", level=logging.INFO)


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url):
        if url.startswith("http"):
            self.driver.get(url)
            logging.info('Opening page "{}"'.format(url))
        else:
            self.driver.get(config.baseurl + url)
            logging.info('Opening page "{}"'.format(config.baseurl + url))

    def _find(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])
        logging.info('Attempting to find element "{}" using method "{}"'.format(locator["value"], locator["by"]))

    def _click(self, locator):
        self._find(locator).click()
        logging.info('Attempting to click element specified with locator "{}"'.format(locator))

    def _type(self, locator, input_text):
        self._find(locator).send_keys(input_text)
        logging.info('Attempting to send text "{}" to element specified with locator "{}"'.format(input_text, locator))

    def _is_displayed(self, locator):
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            logging.info('Element specified with locator "{}" is not visible'.format(locator))
            return False
        logging.info('Element specified with locator "{}" is visible'.format(locator))
        return True

    def wait_for_is_displayed(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.visibility_of_element_located(
                    (locator['by'], locator['value'])
                )
            )
        except TimeoutException:
            logging.info('Element specified with locator "{}" is not visible after {} seconds'.format(locator, timeout))
            return False
        logging.info('Element specified with locator "{}" is visible'.format(locator))
        return True

    def wait_for_title_to_be(self, expected_title, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.title_is(expected_title)
            )
        except TimeoutException:
            logging.info('Current page title "{}" is NOT a match for expected value "{}"'.format(self.driver.title, expected_title))
            return False
        logging.info('Current page title "{}" matches expected value "{}"'.format(self.driver.title, expected_title))
        return True
