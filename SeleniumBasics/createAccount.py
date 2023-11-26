import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class createAccount():

    def creatAccount(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://www.facebook.com/")
        #self.browser.implicitly_wait(10)
        self.browser.find_element(by=By.CSS_SELECTOR,value="[data-testid='open-registration-form-button']").click()
        WebDriverWait(self.browser, 60).until(EC.visibility_of_element_located((By.NAME, "firstname")))

        self.browser.find_element(by=By.NAME, value="firstname").send_keys("sathish")
        time.sleep(3)

obj=createAccount()
obj.creatAccount()