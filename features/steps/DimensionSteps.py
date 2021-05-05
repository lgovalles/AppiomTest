import time

from behave import given
from behave import then
from behave import when

from pageobjects.DimensionPage import DimenstionPage

mainpage = DimenstionPage()

@given(u'I am on the "{menuOption}" page')
def step_impl(context,menuOption):
    print("given")
    mainpage.ClickOnMainMenu()
    mainpage.ClickOnMenuOption(menuOption)


@when(u'I select the Length "{fromLength}" to convert "{toLength}"')
def step_impl(context, fromLength, toLength):
    print("when")
    mainpage.ClickOnFrom()
    mainpage.selectUnit(fromLength)
    mainpage.ClickOnTo()
    mainpage.selectUnit(toLength)


@given("I am on the Area page")
def step_impl(context):
    print("given")
    mainpage.ClickOnMainMenu()
    mainpage.ClickOnMenuOption("Area")


@when(u'I select the Area "{fromArea}" to convert "{toArea}"')
def step_impl(context, fromArea, toArea):
    print("when")
    mainpage.ClickOnFrom()
    mainpage.selectUnit(fromArea)
    mainpage.ClickOnTo()
    mainpage.selectUnit(toArea)


@given("I am on the volume page")
def step_impl(context):
    print("given")
    mainpage.ClickOnMainMenu()
    mainpage.ClickOnMenuOption("Volume")


@when(u'I select the volume "{fromVol}" to convert "{toVol}"')
def step_impl(context, fromVol, toVol):
    print("when")
    mainpage.ClickOnFrom()
    mainpage.selectUnit(fromVol)
    mainpage.ClickOnTo()
    mainpage.selectUnit(toVol)


@then(u'The initial value should be "{iniVal}"')
def step_impl(context, iniVal):
    print("then")
    mainpage.ClickOnClear("C")
    mainpage.ClickOnNumber(iniVal)
    assert iniVal in mainpage.get_valueFrom()
    time.sleep(2)


@then(u'the concert value should "{resVal}"')
def step_impl(context, resVal):
    print("then")
    assert resVal in mainpage.get_valueTo()


@given("I am on the Speed page")
def step_impl(context):
    mainpage.ClickOnMainMenu()
    mainpage.ClickOnMenuOption("Speed")


@when(u'I select the sped "{fromSpeed}" to convert "{toSpeed}"')
def step_impl(context, fromSpeed, toSpeed):
    print("when")
    mainpage.ClickOnFrom()
    mainpage.selectUnit(fromSpeed)
    mainpage.ClickOnTo()
    mainpage.selectUnit(toSpeed)


@then(u'The speed initial value should be "{iniVal}"')
def step_impl(context, iniVal):
    mainpage.ClickOnClear("C")
    mainpage.ClickOnNumber(iniVal)
    assert iniVal in mainpage.get_valueFrom()


@then(u'The speed concert value should be "{resVal}"')
def step_impl(context, resVal):
    assert resVal in mainpage.get_valueTo()