# filename tests/conftest.py

import pytest
import os
from tests import config
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="http://www.34protons.co.uk/demo_2_0",
                     help="base url for application under test"
                     )
    parser.addoption("--geckodriverpath",
                     action="store",
                     default=os.path.join(os.getcwd(), 'vendor', 'geckodriver'),
                     help="path to location of geckodriver executable"
                     )


@pytest.fixture
def driver(request):
    """Returns a Firefox driver instance using geckodriver"""
    config.baseurl = request.config.getoption("--baseurl")
    config.geckodriverpath = request.config.getoption("--geckodriverpath")

    driver_ = webdriver.Firefox(executable_path=config.geckodriverpath)
    yield driver_
    driver_.quit()
