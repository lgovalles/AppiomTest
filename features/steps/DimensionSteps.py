from behave import given
from behave import then
from behave import when

from pageobjects.DimensionPage import DimenstionPage

mainpage = DimenstionPage()

@given("I am on the Length page")
def step_impl(context):
    print("given")
    mainpage.ClickOnMainMenu()
    mainpage.ClickOnLenth()


@when(u'I select the Length "{fromLength}" to convert "{toLength}"')
def step_impl(context, fromLength, toLength):
    print("when")
    mainpage.ClickOnTo()
    mainpage.selectUnit()


@given("I am on the Area page")
def step_impl(context):
    print("given")
    mainpage.ClickOnMainMenu()
    mainpage.ClickOnArea()


@when(u'I select the Area "{fromArea}" to convert "{toArea}"')
def step_impl(context, fromArea, toArea):
    print("when")
    mainpage.ClickOnTo()
    mainpage.selectUnit()


@given("I am on the volume page")
def step_impl(context):
    print("given")
    mainpage.ClickOnMainMenu()
    mainpage.ClickOnVolume()


@when(u'I select the volume "{fromVol}" to convert "{toVol}"')
def step_impl(context, fromVol, toVol):
    print("when")
    mainpage.ClickOnTo()
    mainpage.selectUnit()


@then(u'The initial value should be "{iniVal}"')
def step_impl(context, iniVal):
    print("then")
    assert iniVal in mainpage.get_valueFrom()


@then(u'the concert value should "{resVal}"')
def step_impl(context, resVal):
    print("then")
    assert resVal in mainpage.get_valueTo()


@given("I am on the speed page")
def step_impl(context):
    mainpage.ClickOnMainMenu()
    mainpage.scrollDown()
    mainpage.ClickOnSpeet()


@when(u'I select the sped "{fromSpeed}" to convert "{toSpeed}"')
def step_impl(context, fromSpeed, toSpeed):
    print("when")
    mainpage.ClickOnTo()
    mainpage.selectUnit()


@then(u'The speed initial value should be "{iniVal}"')
def step_impl(context, iniVal):
    assert iniVal in mainpage.get_valueFrom()


@then(u'The speed concert value should be "{resVal}"')
def step_impl(context, resVal):
    assert resVal in mainpage.get_valueTo()