import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class BasePage(object):
    android_cap = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "generic_x86_arm",
        "automationName": "UIAutomator2",
        "app": "D:\\Test\\PreciseUnitConversion.apk"
    }

    def __init__(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.android_cap)

    def __del__(self):
        self.driver.quit()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_driver_android(self):
        return webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.android_cap)

    def scrollDown(self):
        time.sleep(2)
        scrolldown = TouchAction(self.driver)
        scrolldown.press(x=200, y=1568).move_to(x=200, y=557).release().perform()

    def scrollUp(self):
        time.sleep(2)
        scrolldown = TouchAction(self.driver)
        scrolldown.press(x=262, y=237).move_to(x=232, y=893).release().perform()
