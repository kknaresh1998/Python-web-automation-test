from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
import os

import pytest

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_Name", action="store", default="firefox", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_Name = request.config.getoption("browser_Name")
    if browser_Name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.implicitly_wait(30)
    elif browser_Name == "edge":
        #driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver = webdriver.Edge(
            service=EdgeService(executable_path="C:\Program Files\grid\Webdrivers\msedgedriver.exe"))

        driver.implicitly_wait(30)
    else:
        raise ValueError(f"Unsupported browser: {browser_Name}")

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    yield driver
    driver.close() #yield will check after reture driver, Is there any code.

# Hook to capture screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            if not os.path.exists(reports_dir):
                os.makedirs(reports_dir)
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)