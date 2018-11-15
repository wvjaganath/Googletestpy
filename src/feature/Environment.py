from base import browser_chrome
from base import browser_firefox

# Environment variable for running the test

# Executes first when test is run -- Invokes Browser


def before_all(context):
    web = context.config.userdata['browser']
    if web == "firefox":
        browser_firefox(context)
    else:
        browser_chrome(context)

# Closes browser once test is complete


def after_all(context):
    if context.driver is not None:
        context.driver.close()
        context.driver.quit()
