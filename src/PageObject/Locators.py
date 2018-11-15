# Locators for Home and Search page of Google


class Locator(object):

    logo = "//img[@id='hplogo']"

    # Locator for Search field
    srchField = "//input[@name='q']"

    # Locator for Google Search button
    gleBtn = "//div[@class='FPdoLc VlcLAe']//input[@value='Google Search']"

    # Locator for Google Time taken Counter
    timeTaken = "//div[@class='appbar']"

    # Locator for Google Search Results
    srchresults = ".r"