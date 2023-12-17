
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

class mouseandKeyboard():

    def mouseactions(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://www.ebay.com/")
        mouse =ActionChains(self.browser)
        mouse.move_to_element(self.browser.find_element(by=By.XPATH,value="//*[@class='hl-cat-nav__js-tab']//a[text()='Electronics']")).perform()
        mouse.move_to_element(self.browser.find_element(by=By.XPATH,value="//*[text()='Computers and tablets']")).click().perform()
        time.sleep(5)

    def mouseactionswithfb(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://www.facebook.com/")
        mouse = ActionChains(self.browser)
        mouse.move_to_element(self.browser.find_element(by=By.ID,
                                                        value="email")).send_keys("Sathish").double_click().context_click().perform()

    def mouseactionswithdragdrop(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://leafground.com/drag.xhtml")
        mouse = ActionChains(self.browser)
        mouse.move_to_element(self.browser.find_element(by=By.ID,value="form:drag")).drag_and_drop(self.browser.find_element(by=By.ID,value="form:drag"),self.browser.find_element(by=By.ID,value="form:drop_content")).perform()

        time.sleep(5)

    def mouseactionswithdragdropby(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://leafground.com/drag.xhtml")
        mouse = ActionChains(self.browser)
        mouse.move_to_element(self.browser.find_element(by=By.XPATH, value="(//*[contains(@class,'ui-slider-handle')])[1]")).drag_and_drop_by_offset(self.browser.find_element(by=By.XPATH, value="(//*[contains(@class,'ui-slider-handle')])[1]"),40,0).perform()
        mouse.move_to_element(self.browser.find_element(by=By.XPATH,
                                                        value="(//*[contains(@class,'ui-slider-handle')])[2]")).drag_and_drop_by_offset(
        self.browser.find_element(by=By.XPATH, value="(//*[contains(@class,'ui-slider-handle')])[2]"), -40,
            0).perform()
        i =25;
        while(i<60):
            mouse.move_to_element(self.browser.find_element(by=By.XPATH,
                                                            value="(//*[contains(@class,'ui-slider-handle')])[2]")).drag_and_drop_by_offset(
                self.browser.find_element(by=By.XPATH, value="(//*[contains(@class,'ui-slider-handle')])[2]"), -40,
                0).perform()
            i=61;

    def mouseactionswithfbkeyboad(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://www.facebook.com/")
        mouse = ActionChains(self.browser)
        mouse.move_to_element(self.browser.find_element(by=By.ID,
                                                            value="email")).send_keys(
                "Sathish").key_down(Keys.TAB).key_up(Keys.TAB).key_up(Keys.SHIFT).key_up(Keys.TAB).key_down(Keys.SHIFT).key_down(Keys.TAB).perform()

        time.sleep(5)

    def mouseactionswithfbpyautogui(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://www.facebook.com/")
        mouse = ActionChains(self.browser)
        mouse.move_to_element(self.browser.find_element(by=By.ID,value="email")).send_keys("Sathish").double_click().context_click().perform()
        pyautogui.press(['down','down','down'])
        #pyautogui.press('down')
        #pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl','v')

        time.sleep(5)

obj = mouseandKeyboard()
obj.mouseactionswithfbpyautogui()