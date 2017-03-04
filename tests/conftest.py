# filename tests/confttest.py

import pytest
from tests import config
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="http://www.34protons.co.ukdemo_2_0",
                     help="base url for application under test"
                     )
    parser.addoption("--geckodriverpath",
                     action="store",
                     default="os.path.join(os.getcwd(), 'vendor' , 'geckodriver' )",
                     help="path to location of geckodriver executable"
                     )


@pytest.fixture
def driver(request):
    driver_ = webdriver.Firefox(executable_path=config.geckodriverpath)
    yield driver_
    driver_.quit()
