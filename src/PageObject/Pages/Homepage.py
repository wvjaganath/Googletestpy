from selenium.common.exceptions import NoSuchElementException


from src.PageObject.Locators import Locator
from selenium.webdriver.common.by import By


class Home(object):

    def __init__(self, driver):
        self.driver = driver

        # Defining Locators

        self.logo = driver.find_element(By.XPATH, Locator.logo)
        self.srchField = driver.find_element(By.XPATH, Locator.srchField)
        self.gleBtn = driver.find_element(By.XPATH, Locator.gleBtn)

    def getLogo(self):
        return self.logo

    def srch(self):
        return self.srchField

    def nosrch(self):
        self.gleBtn.click()

    def srchtxt(self, text):
        self.srchField.send_keys(text)
        element_attribute_value = self.srchField.get_attribute("value")
        print element_attribute_value

    def button(self):
        return self.gleBtn


