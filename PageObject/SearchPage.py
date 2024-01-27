import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from CommonUtilities.CommonElements import CommonElements


class SearchPage(CommonElements):

    def __init__(self,browser):
        self.browser = browser

    def SelectFromValueFromDropDown(self,fromValue):
        self.WaitForElementToBeClickable(self.browser,"//*[@for='fromCity']")
        self.browser.find_element(by=By.XPATH, value="//*[@for='fromCity']").click()

        WebDriverWait(self.browser, 60).until(EC.element_to_be_clickable((By.XPATH, "(//ul[@role='listbox']//li)[1]")))
        # Select value from From location
        Allfromlocation = self.browser.find_elements(by=By.XPATH, value="//ul[@role='listbox']//li")
        for eachElement in Allfromlocation:
            fromlocationCode = eachElement.find_element(By.CSS_SELECTOR,
                                                        value="div[class*='makeFlex']>div[class*='pushRight']").text
            if (fromlocationCode == fromValue):
                eachElement.click()
                return self.browser.find_element(by=By.XPATH, value="//*[@data-cy='fromCity']").get_attribute("value")

    def SelectToValueFromDropdown(self, toValue):
        self.WaitForPresenceOfelement(self.browser, "//*[@for='toCity']")
        self.browser.find_element(by=By.XPATH, value="//*[@for='toCity']").click()
        #self.WaitForElementToBeClickable(self.browser, "(//ul[@role='listbox']//li)[1]")

        WebDriverWait(self.browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, "(//ul[@role='listbox']//li)[1]")))

        Allfromlocation = self.browser.find_elements(by=By.XPATH, value="//ul[@role='listbox']//li")
        for eachElement in Allfromlocation:
            fromlocationCode = eachElement.find_element(By.CSS_SELECTOR,
                                                        value="div[class*='makeFlex']>div[class*='pushRight']").text
            if (fromlocationCode == toValue):
                eachElement.click()
                return self.browser.find_element(by=By.XPATH, value="//*[@data-cy='toCity']").get_attribute("value")

    def SelectDepatureDate(self,dateToBeSelect):
        basePath = "((//*[@class='DayPicker-Month'])[last()-1]//*[@class='DayPicker-Week']//div[contains(@class,'DayPicker-Day')])"
        WebDriverWait(self.browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, basePath)))

        AllDates = self.browser.find_elements(by=By.XPATH, value=basePath);
        for i in range(1, len(AllDates) + 1):

            dateIsDisabled = self.browser.find_element(by=By.XPATH, value=basePath + "[" + str(i) + "]").get_attribute(
                "class")
            if (not dateIsDisabled.__contains__("disabled")):
                elementExist = self.browser.find_elements(by=By.XPATH, value=basePath + "[" + str(i) + "]//p")
                if (len(elementExist) > 0):
                    actualDate = self.browser.find_element(by=By.XPATH, value=basePath + "[" + str(i) + "]//p").text
                    print(actualDate)
                    if (int(actualDate) == (int(dateToBeSelect))):
                        self.browser.find_element(by=By.XPATH, value=basePath + "[" + str(i) + "]").click()
                        break

    def ClickOnSearchButton(self):
        WebDriverWait(self.browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Search']")))

        #self.browser.find_element(by=By.XPATH, value="//*[text()='Search']").click()
        self.ClickOnElement(self.browser,By.XPATH,"//*[text()='Search']")

    def RetrieveErrorText(self):
        self.WaitForPresenceOfelement(self.browser,"//*[@data-cy='sameCityError']")
        errortext = self.browser.find_element(by=By.XPATH, value="//*[@data-cy='sameCityError']").text
        print(errortext)
        return errortext