from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Base file containing browser drivers


# To get current working directory
cwd = os.path.dirname(__file__)

# For Firefox


def browser_firefox(context):
    context.driver = webdriver.Firefox(
        executable_path=cwd+"/resources/drivers/geckodriver")
    context.driver.maximize_window()

# For Chrome
# Added extra arguments as Chrome has some issues starting in Maximize mode


def browser_chrome(context):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument('window-size=2560,1440')
    context.driver = webdriver.Chrome(
        executable_path=cwd+"/resources/drivers/chromedriver", chrome_options=options)

