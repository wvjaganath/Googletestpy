from base import browser_chrome
from base import browser_firefox


def before_all(context):
    web = context.config.userdata['browser']
    if web == "firefox":
        browser_firefox(context)
    else:
        browser_chrome(context)



def after_all(context):
    if context.driver is not None:
        context.driver.close()
        context.driver.quit()
