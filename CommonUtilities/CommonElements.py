from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class CommonElements():
    popUpElement = "//*[@class='close']"

    def ClickPopIfExist(self,browser):
        allframeelement = browser.find_elements(by=By.TAG_NAME,value="iframe")
        if(len(allframeelement)>0):
            for eachFrame in range(0,len(allframeelement)):
                browser.switch_to.frame(eachFrame)
                elementexist = browser.find_elements(by=By.XPATH, value=self.popUpElement);
                if(len(elementexist) > 0):
                    for eachelement in elementexist:
                        eachelement.click()
                        break
                browser.switch_to.default_content()

    def WaitForPresenceOfelement(self,browser,element):
        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, element)))

    def WaitForElementToBeClickable(self,browser,element):
        WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, element)))

    def ClickOnElement(self ,browser,locator,element):
        actualelement = browser.find_element(by=locator,value=element)
        actualelement.click()
