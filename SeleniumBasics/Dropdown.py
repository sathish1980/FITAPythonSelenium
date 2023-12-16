import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class dropdown():

    def creatAccount(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://www.facebook.com/")
        self.browser.find_element(by=By.CSS_SELECTOR, value="[data-testid='open-registration-form-button']").click()
        WebDriverWait(self.browser, 60).until(EC.visibility_of_element_located((By.NAME, "firstname")))

        self.browser.find_element(by=By.NAME, value="firstname").send_keys("sathish")
        dayDropdown = Select(self.browser.find_element(by=By.ID,value="day"))
        dayDropdown.select_by_index(4)
        monthDropdown = Select(self.browser.find_element(by=By.ID, value="month"))
        monthDropdown.select_by_value("6")
        yearDropdown = Select(self.browser.find_element(by=By.ID, value="year"))
        yearDropdown.select_by_visible_text("2009")
        time.sleep(3)

    def multiselectDropdown(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
        food = Select(self.browser.find_element(by=By.XPATH,value="//select[@id='second']"))
        if(food.is_multiple):
            food.select_by_index(3)
            #time.sleep(1)
            food.select_by_visible_text("Donut")
            #time.sleep(1)
            food.select_by_value("pizza")
            #time.sleep(1)
            food.deselect_by_index(3)
            #time.sleep(1)
            food.deselect_all()

        time.sleep(3)

obj=dropdown()
obj.multiselectDropdown()
