import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class seleniumFirstclass():
    browser= "null"
    def launch(self):
        self.browser =webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        #browser.minimize_window()
        self.browser.get("https://www.facebook.com/")
        """self.browser.get("https://www.gmail.com/")
        self.browser.back()
        self.browser.forward()
        self.browser.refresh()"""
        self.browser.find_element(by=By.ID, value="email").send_keys("kumar")
        #By ID
        #username = self.browser.find_element(by=By.ID,value="email")
        #By Name
        username = self.browser.find_element(by=By.NAME, value="email")
        #By Class Name
        #username = self.browser.find_element(by=By.CLASS_NAME, value="inputtext _55r1 _6luy")

        #username.clear()
        username.send_keys("sathish")
        #by Link Text
        #self.browser.find_element(by=By.LINK_TEXT,value="Forgotten password?").click()
        #By partial link text
        self.browser.find_element(by=By.PARTIAL_LINK_TEXT, value="ten passw").click()
        #By css selector with tag and id
        self.browser.find_element(by=By.CSS_SELECTOR, value="input#email").send_keys("btech")
        # By css selector with tag and class
        #self.browser.find_element(by=By.CSS_SELECTOR, value="input.email").send_keys("btech")
        # By css selector with tag and Attribute
        self.browser.find_element(by=By.CSS_SELECTOR, value="input[data-testid='royal_email']").send_keys("btech")
        # By css selector with tag class and Attribute
        self.browser.find_element(by=By.CSS_SELECTOR, value="iinput.inputtext _55r1 _6luy[data-testid='royal_email']").send_keys("btech")

        time.sleep(3)
        #browser.close()
        #browser.quit()
    def launch2(self):
        self.browser.refresh()

obj= seleniumFirstclass()
obj.launch()