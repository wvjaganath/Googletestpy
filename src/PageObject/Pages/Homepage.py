from selenium.common.exceptions import NoSuchElementException


from src.PageObject.Locators import Locator
from selenium.webdriver.common.by import By

# Homepage Page Objects


class Home(object):

    def __init__(self, driver):
        self.driver = driver

        # Defining Locators

        self.logo = driver.find_element(By.XPATH, Locator.logo)
        self.srchField = driver.find_element(By.XPATH, Locator.srchField)
        self.gleBtn = driver.find_element(By.XPATH, Locator.gleBtn)

# Find element for Logo
# Added a Try/Catch condition if Google changes the logo name
    def getLogo(self):
        try:
            self.logo = self.driver.find_element(By.XPATH, Locator.logo)

        except NoSuchElementException:
            print("\n Googele Search is not present or has been changed")
        return self.logo


# Find elemnt for Search field
    def srch(self):
        return self.srchField

# Find element for Search button

    def button(self):
        return self.gleBtn

# click on Search button
    def nosrch(self):
        self.gleBtn.click()

# TO enter text on the search field and get the entered value for verification

    def srchtxt(self, text):
        self.srchField.send_keys(text)
        element_attribute_value = self.srchField.get_attribute("value")
        print "\n " + element_attribute_value + "\n "





