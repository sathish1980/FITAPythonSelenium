import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class webtable():

    def tableimplementation(self,expectedCoutnry):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://leafground.com/table.xhtml")
        #total pages
        totalPage = self.browser.find_elements(by=By.XPATH,value="//*[@class='ui-paginator-pages']//a")
        for eachpage in range(1,len(totalPage)+1):
            self.browser.find_element(by=By.XPATH, value="//*[@class='ui-paginator-pages']//a["+str(eachpage)+"]").click()
            time.sleep(2)

            allrows = self.browser.find_elements(by=By.XPATH,value="//*[@id='form:j_idt89']//table//tbody[@id='form:j_idt89_data']//tr")
            for i in range(1,len(allrows)):
                actualCountry = self.browser.find_element(by=By.XPATH,
                                       value="//*[@id='form:j_idt89']//table//tbody[@id='form:j_idt89_data']//tr["+str(i)+"]//td[2]//span[3]").text
                #print(actualCountry)
                if expectedCoutnry == actualCountry :
                    name = self.browser.find_element(by=By.XPATH,
                                          value="//*[@id='form:j_idt89']//table//tbody[@id='form:j_idt89_data']//tr[" + str(
                                              i) + "]//td[1]").text
                    print ("**********", "matched")
                    print(name)

        time.sleep(10)


obj =webtable()
obj.tableimplementation("India")
