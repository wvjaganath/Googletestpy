from behave import *
from selenium.common.exceptions import NoSuchElementException

from src.PageObject.Pages.Homepage import Home
from src.PageObject.Pages.Searchpage import Search

# Step file containing the feature definition


@given('user navigates to homepage of Google "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    #context.driver.implicitly_wait(10)


@then("logo should be displayed")
def step_impl(context):
    m = Home(context.driver)

    if m.getLogo().is_displayed():
        print "\n Google search logo is present"


@step("search text field should be displayed")
def step_impl(context):
    m1 = Home(context.driver)

    if m1.srch().is_displayed():
        print "\n Google search text field is present"


@step("Google search button should be present")
def step_impl(context):
    m2 = Home(context.driver)

    if m2.button().is_displayed():
        print "\n Google search button is present"


@step("Blank text should not preform search")
def step_impl(context):
    m3 = Search(context.driver)
    m3.srchblank()


@step("Check if text can be entered in search field")
def step_impl(context):
    m4 = Home(context.driver)

    m4.srchtxt("wikipedia")


@then("Clicking on search button shows results")
def step_impl(context):
    m5 = Home(context.driver)
    m5.nosrch()

    m6 = Search(context.driver)
    print m6.srchtext
