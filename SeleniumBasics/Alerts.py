
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class Alerts1():

    def Alerts1implementation(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://leafground.com/alert.xhtml")
        self.browser.find_element(by=By.ID,value="j_idt88:j_idt91").click()
        self.browser.switch_to.alert.accept()

        actualText = self.browser.find_element(by=By.XPATH, value="//*[@id='j_idt88:j_idt91']//parent::div//span[@id='simple_result']").text
        print(actualText)

        # confirm
        self.browser.find_element(by=By.ID, value="j_idt88:j_idt93").click()
        print(self.browser.switch_to.alert.text)
        self.browser.switch_to.alert.dismiss()
        actualText = self.browser.find_element(by=By.XPATH,
                                               value="//*[@id='j_idt88:j_idt93']//parent::div//span[@id='result']").text
        print(actualText)

    time.sleep(3)

obj=Alerts1()
obj.Alerts1implementation()




