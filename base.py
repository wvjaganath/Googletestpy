from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

cwd = os.path.dirname(__file__)

print cwd


def browser_firefox(context):
    context.driver = webdriver.Firefox(
        executable_path=cwd+"/resources/drivers/geckodriver")
    context.driver.maximize_window()


def browser_chrome(context):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument('window-size=2560,1440')
    context.driver = webdriver.Chrome(
        executable_path=cwd+"/resources/drivers/chromedriver",chrome_options=options)

