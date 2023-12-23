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


class windows():

    def Windowsimplementation(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://leafground.com/window.xhtml")
        parentwindows =self.browser.current_window_handle
        self.browser.find_element(by=By.ID,value="j_idt88:new").click()
        alwindows = self.browser.window_handles

        for eachwindow in alwindows:

            if(eachwindow!=parentwindows):
                self.browser.switch_to.window(eachwindow)
                elementExist = self.browser.find_elements(by=By.ID,
                                                          value="menuform:j_idt40")
                if len(elementExist) > 0:
                    self.browser.find_element(by=By.ID,
                                              value="menuform:j_idt40").click()
                    self.browser.find_element(by=By.ID,value="menuform:m_input").click()
                    self.browser.find_element(by=By.ID,value="j_idt88:name").send_keys("sathish")
                    self.browser.quit()
            #self.browser.switch_to.window(parentwindows)
        time.sleep(10)

obj = windows()
obj.Windowsimplementation()