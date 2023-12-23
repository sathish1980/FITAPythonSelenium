import time

import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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


class uplod:

    def upl(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://cleartax.in/paytax/UploadForm16")
        self.driver.maximize_window()
        self.driver.find_element(by=By.XPATH,value="(//div[@class='input-file-upload-hover-placeholder']//parent::div)[1]").click()
        pyperclip.copy("D:\\Besant\\API\\api.pdf")
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        print("uploaded sucessfully")
        time.sleep(10)

e =uplod()
e.upl()