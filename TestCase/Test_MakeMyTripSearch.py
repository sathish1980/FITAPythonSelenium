import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from Base.BaseClass import BaseClass
from PageObject.SearchPage import SearchPage
from PageObject.SearchResultPage import SearchResultPage


class Test_MakeMyTripSearch(BaseClass):

    browser ="null"
    URL = "https://www.makemytrip.com/"
    samecityError ="From & To airports cannot be the same"
    flightSearchText ="Flights from Bengaluru to Chennai"

    def test_ValidFlightSearch(self):
        self.browser.get(self.URL)
        # click popup if exist
        #self.ClickPopIfExist(self.browser,self.popUpElement)
        sp = SearchPage(self.browser)
        sp.ClickPopIfExist(self.browser)
        # Click FromLocation and Select Value
        sp.SelectFromValueFromDropDown("BLR")
        # Click ToLocation and Select Value
        sp.SelectToValueFromDropdown("MAA")
        # Select Date
        sp.SelectDepatureDate("15")
        #Click on search button
        sp.ClickOnSearchButton()
        # wait and click on ok got it popup
        srp = SearchResultPage(self.browser)
        srp.ClickOnOkGotItPopup()
        # reterive search text
        actualText =srp.GetSearchText()
        assert self.flightSearchText ==actualText
        time.sleep(2)
        print("done")


    def test_FlightSearchWithSameCity(self):
        self.browser.back()
        self.browser.get(self.URL)
        # Click ToLocation and Select Value
        sp =SearchPage(self.browser)
        sp.SelectToValueFromDropdown("BLR")
        # get the Same city validation error
        actualText = sp.RetrieveErrorText()
        assert self.samecityError == actualText
        print("done")



