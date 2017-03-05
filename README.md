# 34-protons-python-automation

### Installation

This is a demo project showcasing the use of Python and Selenium/WebDriver in test automation.
Pre-requisites are selenium (3+) and pytest
```
pip install selenium, pytest
```
The results of running _pip freeze_ were;

```
pytest==3.0.6
selenium==3.0.2
```

Having installed the required packages clone the git repository.

As of the time of writing the version of _geckodriver_ contained in the _vendor_ directory was
```
$./vendor/geckodriver --version
geckodriver 0.14.0
```
Depending on your currently installed version of _Firefox_ you may need to copy a newer version into this directory. Geckodriver releases are available from;
 
 https://github.com/mozilla/geckodriver/releases

Run the tests from within the cloned directory (see _Running tests from the commandline_ below).

This code was validated with _geckodriver(0.14.0)_ and _Firefox(51.0.1)_ on _macOS 10.12.3_.
### Project Structure
```
├── README.md
├── pages
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── main_page.py
├── tests
│   ├── __init__.py
│   ├── config.py
│   ├── conftest.py
│   ├── login_test.py
│   └── mainpage_test.py
├── vendor
│   └── geckodriver
```
The project is so structured that tests and config files are located in the _tests_ directory and automation code is located in the _pages_ directory. The _vendors_ directory contains various browser driver files.

### Configuration

_conftest.py_

Contains a fixture that creates a Firefox driver instance

```
@pytest.fixture
def driver(request):
    """Returns a Firefox driver instance using geckodriver"""
    # Set config properties (either command line or default)
    config.baseurl = request.config.getoption("--baseurl")
    config.geckodriverpath = request.config.getoption("--geckodriverpath")

    driver_ = webdriver.Firefox(executable_path=config.geckodriverpath)
    yield driver_
    driver_.quit()
```
Other fixtures are added to _test_ pages to return relevant instances of the page objects are required.

Adding a _docstring_ to the fixture helps when running the _pytest --fixtures_ command as it returns information about the purpose of each one.

This module contains code that evaluates any commandline parameters and updates the config values with the passed in values or, in their absence, the specified defaults.

```
def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="http://www.34protons.co.uk/demo_2_0",
                     help="base url for application under test"
                     )
```

_config.py_

A useful place to store values that can be accessed by importing the config.py.
```
from tests import config
```

### Running tests from the commandline

Running _pytest_ from the command prompt will cause all tests below the directory to be run. To avoid this pass in the path to the directory where the required tests are located.

```
$pytest ./tests
============================================================== test session starts =============
platform darwin -- Python 3.5.2, pytest-3.0.6, py-1.4.32, pluggy-0.4.0
rootdir: /Users/stevemckinney/Documents/Workspace/34-protons-python-automation, inifile:
collected 3 items

tests/login_test.py ..
tests/mainpage_test.py .

=========================================================== 3 passed in 17.18 seconds ==========
```

Passing in the _-v_ flag gives _verbose_ output. Compare this with the _-q_ flag that provides minimal output.

```
$pytest -v ./tests
============================================================== test session starts =============
platform darwin -- Python 3.5.2, pytest-3.0.6, py-1.4.32, pluggy-0.4.0 -- /Users/stevemckinney
/Documents/Workspace/34-protons-python-automation/venv/bin/python3.5
cachedir: .cache
rootdir: /Users/stevemckinney/Documents/Workspace/34-protons-python-automation, inifile:
collected 3 items

tests/login_test.py::TestLogin::test_displays_page_loading_with_valid_credentials PASSED
tests/login_test.py::TestLogin::test_main_page_loads PASSED
tests/mainpage_test.py::TestMainPage::test_mainpage_displays_correct_title PASSED

=========================================================== 3 passed in 17.18 seconds ==========

$pytest -q ./tests
...
3 passed in 18.92 seconds
```

Passing in the _-s_ option _turns off_ output capture allowing print statements to be displayed.

```
collected 3 items

tests/login_test.py Created instance of login page
.Created instance of login page
.
tests/mainpage_test.py Created instance of main page
.
```

The following commandline options can be specified

* _--baseurl_
* _--geckodriverpath_

These allow tests to be run using a different baseurl (i.e a locally hosted copy or a different geckodriver version) whilst maintaining default values.

```
$ pytest --baseurl=http://localhost ./tests
```

### Logging

The project uses the Python logging module. By default logs are written to the file _test.log_ in the root of the project directory

Information about the current test being run is found in the _request.node_ object.

Properties currently include

* _name_ (the name of the test method e.g. _test_main_page_loads_after_valid_credentials_supplied_)
* _location[0]_ (path to file containing test method)