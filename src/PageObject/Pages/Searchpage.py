import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from src.PageObject.Locators import Locator


# Search Page Objects


class Search(object):

    def __init__(context, driver):
        context.driver = driver

# To find if the Timetaken element present or not
    def srchblank(context):
        try:
            context.timeTaken = context.driver.find_element(By.XPATH, Locator.timeTaken)

        except NoSuchElementException:
            print("\n Search not performed")


# To find the Count of Results  for successful search
    @property
    def srchtext(context):
       try:
            ui.WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locator.srchresults)))
            srchresults = context.driver.find_elements(By.CSS_SELECTOR, Locator.srchresults)
            return len(srchresults)
       except TimeoutException:
           print("\n Search not performed")


