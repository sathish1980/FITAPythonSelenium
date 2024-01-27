import logging
import time



from Base.BaseClass import BaseClass
from PageObject.SearchPage import SearchPage
from PageObject.SearchResultPage import SearchResultPage


class Test_MakeMyTripSearch(BaseClass):


    browser ="null"
    URL = "https://www.makemytrip.com/"
    samecityError ="From & To airports cannot be the same"
    flightSearchText ="Flights from pune to Chennai"

    def BrowserLaunch(self):
        log = self.getLogger()
        self.browser.get(self.URL)
        log.warning("maximized")
        log.info("Browser is Launched")

    def test_ValidFlightSearch(self,SeachWithParameter):
        log = self.getLogger()
        self.BrowserLaunch()
        total_value = len(SeachWithParameter)
        keyvalue=total_value/3
        print("the length of dict is : ",len(SeachWithParameter))
        # click popup if exist
        #self.ClickPopIfExist(self.browser,self.popUpElement)
        sp = SearchPage(self.browser)
        time.sleep(4)
        #sp.ClickPopIfExist(self.browser)
        log.info("popup is clicked")
        # Click FromLocation and Select Value
        for eachValue in range(2,keyvalue+1):
            print(SeachWithParameter["FromLocation"+str(eachValue)])
            sp.SelectFromValueFromDropDown(SeachWithParameter["FromLocation"+str(eachValue)])
            log.info("selected the from value")
            # Click ToLocation and Select Value
            sp.SelectToValueFromDropdown(SeachWithParameter["ToLocation"+str(eachValue)])
            log.info("selected the to value")
            # Select Date
            sp.SelectDepatureDate(SeachWithParameter["Date"+str(eachValue)])
            log.info("Selected date value")
            #Click on search button
            sp.ClickOnSearchButton()
            log.info("Clicked on search button")
            # wait and click on ok got it popup
            srp = SearchResultPage(self.browser)
            srp.ClickOnOkGotItPopup()
            log.info("Popup exist")
            # reterive search text
            actualText =srp.GetSearchText()
            #assert self.flightSearchText ==actualText
            time.sleep(2)
            self.browser.back()
            log.info("Assertion done")


    def test_FlightSearchWithSameCity(self,ValidSearch):
        log = self.getLogger()
        self.browser.get(self.URL)
        log.info("URL is Launched")
        # Click ToLocation and Select Value
        sp =SearchPage(self.browser)
        sp.SelectToValueFromDropdown(ValidSearch[0])
        log.info("From location is selected")
        # get the Same city validation error
        actualText = sp.RetrieveErrorText()
        assert self.samecityError == actualText
        log.info("Error validation is done ")



