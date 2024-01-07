from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from CommonUtilities.CommonElements import CommonElements


class SearchResultPage(CommonElements):

    def __init__(self,browser):
        self.browser=browser


    def ClickOnOkGotItPopup(self):
        WebDriverWait(self.browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='overlay']//span)[1]")))

        self.browser.find_element(by=By.XPATH, value="(//div[@class='overlay']//span)[1]").click()

    def GetSearchText(self):
        WebDriverWait(self.browser, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'journey-title')]//span")))

        expectedvalue = self.browser.find_element(by=By.XPATH, value="//*[contains(@class,'journey-title')]//span").text
        print(expectedvalue)
        return expectedvalue


