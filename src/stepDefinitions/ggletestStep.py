from pytest_bdd import scenario, given, when, then


@given('user navigates to homepage "https://www.google.com" of Google')
def step_impl():


@then("logo should be displayed")
def step_impl():
    raise NotImplementedError(u'STEP: Then logo should be displayed')


@given("search text field should be displayed")
def step_impl():
    raise NotImplementedError(u'STEP: And search text field should be displayed')


@given("Google search button should be present")
def step_impl():
    raise NotImplementedError(u'STEP: And Google search button should be present')


@given("Blank text should not preform")
def step_impl():
    raise NotImplementedError(u'STEP: And Blank text should not preform')


@given("Check if text can be entered in search field")
def step_impl():
    raise NotImplementedError(u'STEP: And Check if text can be entered in search field')


@then("Clicking on search button shows results")
def step_impl():
    raise NotImplementedError(u'STEP: Then Clicking on search button shows results')