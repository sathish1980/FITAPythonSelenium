
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
class list():

    def listimplementation(self,expectedCountryName):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://leafground.com/select.xhtml")
        self.browser.find_element(by=By.XPATH,value="//*[@id='j_idt87:country']//div[contains(@class,'ui-selectonemenu-trigger')]").click()
        WebDriverWait(self.browser, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='j_idt87:country_items']//li[last()]")))
        allcountries = self.browser.find_elements(by=By.XPATH,value="//*[@id='j_idt87:country_items']//li")
        for eachcountry in allcountries:
            actualCountryName = eachcountry.text
            if actualCountryName==expectedCountryName:
                print(actualCountryName)
                eachcountry.click()
                break

        time.sleep(3)

obj=list()
obj.listimplementation("USA")
