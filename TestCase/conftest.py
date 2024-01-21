

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Utils.MakeMyTripTestDataRead import MakeMyTripTestDataRead

browser = None

@pytest.fixture(scope="class")
def before():
    print("beforeeach test case")
    yield
    print("after each test case")

@pytest.fixture()
def before1():
    print("before1 each test case")
    yield
    print("after1 each test case")

@pytest.fixture()
def LoadData():
    return ["sathish","kumar","R"]

@pytest.fixture()
def ValidSearch():
    return ["PNQ","MAA","24"]

@pytest.fixture(params={"sathish","kumar","R","K"})
def LoadDatawithParam(request):
    return request.param

@pytest.fixture(params=[("sathish","kumar"),("raja","H")])
def LoadDatawithtuple(request):
    return request.param

@pytest.fixture(params=[("MAA","BLR","24"),("PNQ","MAA","27")])
def SearchWithMultiDate(request):
    return request.param

@pytest.fixture(params=[{"username" : "sathish","password" : "kumar"},{"username" : "raja","password": "H"}])
def LoadDatawithdic(request):
    return request.param

@pytest.fixture(params=[MakeMyTripTestDataRead.excelFileRead("ValidSearch")])
def SeachWithParameter(request):
    return request.param


@pytest.fixture(scope="class")
def OpenBrowser(request):
    global browser
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.maximize_window()
    request.cls.browser=browser
    yield
    browser.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        browser.get_screenshot_as_file("./Report/"+name)
