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


class Frames():

    def Frameimplementation(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://leafground.com/frame.xhtml")
        #self.browser.switch_to.frame("frame2")
        totalFrame = self.browser.find_elements(by=By.TAG_NAME, value="iframe")

        for i in range(0,len(totalFrame)):
            self.browser.switch_to.frame(i)
            totalinnerFrame = self.browser.find_elements(by=By.TAG_NAME, value="iframe")
            if len(totalinnerFrame)>0 :
                self.browser.switch_to.frame("frame2")
                elementExist = self.browser.find_elements(by=By.XPATH, value="//button[@id='Click' and contains(@style,'4b7ecf')]")
                if len(elementExist)>0:
                    self.browser.find_element(by=By.XPATH, value="//button[@id='Click' and contains(@style,'4b7ecf')]").click()
            self.browser.switch_to.default_content()
        time.sleep(10)

obj= Frames()
obj.Frameimplementation()
