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


class Test_MakeMyTripSearch(BaseClass):

    browser ="null"
    URL = "https://www.makemytrip.com/"
    popUpElement = "//*[@class='close']"
    samecityError ="From & To airports cannot be the same"
    flightSearchText ="Flights from Bengaluru to Chennai"

    def test_ValidFlightSearch(self):
        self.browser.get(self.URL)
        # click popup if exist
        self.ClickPopIfExist(self.browser,self.popUpElement)
        # Click FromLocation and Select Value
        self.SelectFromValueFromDropDown(self.browser,"BLR")
        # Click ToLocation and Select Value
        self.SelectToValueFromDropdown(self.browser,"MAA")
        # Select Date
        self.SelectDepatureDate(self.browser,"15")
        #Click on search button
        self.ClickOnSearchButton(self.browser)
        # wait and click on ok got it popup
        self.ClickOnOkGotItPopup(self.browser)
        # reterive search text
        actualText =self.GetSearchText(self.browser)
        assert self.flightSearchText ==actualText
        time.sleep(2)
        print("done")


    def test_FlightSearchWithSameCity(self):
        self.browser.back()
        self.browser.get(self.URL)
        # Click ToLocation and Select Value
        self.SelectToValueFromDropdown(self.browser, "BLR")
        # get the Same city validation error
        actualText = self.RetrieveErrorText(self.browser)
        assert self.samecityError == actualText
        print("done")

    def ClickPopIfExist(self,browser,element):
        allframeelement = browser.find_elements(by=By.TAG_NAME,value="iframe")
        if(len(allframeelement)>0):
            for eachFrame in range(0,len(allframeelement)):
                browser.switch_to.frame(eachFrame)
                elementexist = browser.find_elements(by=By.XPATH, value=element);
                if(len(elementexist) > 0):
                    for eachelement in elementexist:
                        eachelement.click()
                        break
                browser.switch_to.default_content()

    def SelectFromValueFromDropDown(self,browser,fromValue):
        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, "//*[@for='fromCity']")))
        browser.find_element(by=By.XPATH, value="//*[@for='fromCity']").click()

        WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "(//ul[@role='listbox']//li)[1]")))
        # Select value from From location
        Allfromlocation = browser.find_elements(by=By.XPATH, value="//ul[@role='listbox']//li")
        for eachElement in Allfromlocation:
            fromlocationCode = eachElement.find_element(By.CSS_SELECTOR,
                                                        value="div[class*='makeFlex']>div[class*='pushRight']").text
            if (fromlocationCode == fromValue):
                eachElement.click()
                return browser.find_element(by=By.XPATH, value="//*[@data-cy='fromCity']").get_attribute("value")

    def SelectToValueFromDropdown(self, browser, toValue):

        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@for='toCity']")))
        browser.find_element(by=By.XPATH, value="//*[@for='toCity']").click()

        WebDriverWait(browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, "(//ul[@role='listbox']//li)[1]")))

        Allfromlocation = browser.find_elements(by=By.XPATH, value="//ul[@role='listbox']//li")
        for eachElement in Allfromlocation:
            fromlocationCode = eachElement.find_element(By.CSS_SELECTOR,
                                                        value="div[class*='makeFlex']>div[class*='pushRight']").text
            if (fromlocationCode == toValue):
                eachElement.click()
                return browser.find_element(by=By.XPATH, value="//*[@data-cy='toCity']").get_attribute("value")

    def SelectDepatureDate(self,browser,dateToBeSelect):
        basePath = "((//*[@class='DayPicker-Month'])[last()-1]//*[@class='DayPicker-Week']//div[contains(@class,'DayPicker-Day')])"
        WebDriverWait(browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, basePath)))

        AllDates = browser.find_elements(by=By.XPATH, value=basePath);
        for i in range(1, len(AllDates) + 1):

            dateIsDisabled = browser.find_element(by=By.XPATH, value=basePath + "[" + str(i) + "]").get_attribute(
                "class")
            if (not dateIsDisabled.__contains__("disabled")):
                elementExist = browser.find_elements(by=By.XPATH, value=basePath + "[" + str(i) + "]//p")
                if (len(elementExist) > 0):
                    actualDate = browser.find_element(by=By.XPATH, value=basePath + "[" + str(i) + "]//p").text
                    print(actualDate)
                    if (int(actualDate) == (int(dateToBeSelect))):
                        browser.find_element(by=By.XPATH, value=basePath + "[" + str(i) + "]").click()
                        break

    def ClickOnSearchButton(self,browser):
        WebDriverWait(browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Search']")))

        browser.find_element(by=By.XPATH, value="//*[text()='Search']").click()

    def ClickOnOkGotItPopup(self,browser):
        WebDriverWait(browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='overlay']//span)[1]")))

        browser.find_element(by=By.XPATH, value="(//div[@class='overlay']//span)[1]").click()

    def GetSearchText(self,browser):
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'journey-title')]//span")))

        expectedvalue = browser.find_element(by=By.XPATH, value="//*[contains(@class,'journey-title')]//span").text
        print(expectedvalue)
        return expectedvalue


    def RetrieveErrorText(self,browser):
        errortext = browser.find_element(by=By.XPATH, value="//*[@data-cy='sameCityError']").text
        print(errortext)
        return errortext