import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


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

@pytest.fixture(params={"sathish","kumar","R","K"})
def LoadDatawithParam(request):
    return request.param

@pytest.fixture(params=[("sathish","kumar"),("raja","H")])
def LoadDatawithtuple(request):
    return request.param

@pytest.fixture(params=[{"username" : "sathish","password" : "kumar"},{"username" : "raja","password": "H"}])
def LoadDatawithdic(request):
    return request.param

@pytest.fixture(scope="class")
def OpenBrowser(request):
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.maximize_window()
    request.cls.browser=browser
    yield
    browser.close()
