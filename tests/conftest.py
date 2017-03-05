# filename tests/conftest.py

import pytest
import os
from tests import config
from selenium import webdriver
import logging
logging.basicConfig(filename="test.log", level=logging.INFO)


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


def create_log_headers(request):
    logging.info('\nStarting test: {}\nContained in file {}'.format(request.node.name, request.node.location[0]))


@pytest.fixture
def driver(request):
    """Returns a Firefox driver instance using geckodriver"""
    config.baseurl = request.config.getoption("--baseurl")
    config.geckodriverpath = request.config.getoption("--geckodriverpath")

    create_log_headers(request)
    driver_ = webdriver.Firefox(executable_path=config.geckodriverpath)
    yield driver_
    driver_.quit()
