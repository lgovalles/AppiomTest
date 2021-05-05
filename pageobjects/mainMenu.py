import time

from selenium.webdriver.common.by import By

from pageobjects.Base_Page import BasePage


class mainMenu(BasePage):
    MENU_BUTTON = (By.XPATH, "//android.widget.ImageButton[@content-desc='Open navigation drawer']")
    SPEED_OPTION = (By.XPATH,
                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.DrawerLayout/android.widget.ListView/android.widget.RelativeLayout[10]/android.widget.RelativeLayout[2]")
    LENGTH_OPTION = (By.XPATH,
                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.DrawerLayout/android.widget.ListView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout[2]")
    VOLUME_OPTION = (By.XPATH,
                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.DrawerLayout/android.widget.ListView/android.widget.RelativeLayout[6]/android.widget.RelativeLayout")
    AREA_OPTION = (By.XPATH,
                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.DrawerLayout/android.widget.ListView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout")

    def ClickOnMainMenu(self):
        self.find_element(*self.MENU_BUTTON).click()

    def ClickOnArea(self):
        self.find_element(*self.AREA_OPTION).click()

    def ClickOnLength(self):
        self.find_element(*self.LENGTH_OPTION).click()

    def ClickOnVolume(self):
        self.find_element(*self.VOLUME_OPTION).click()

    def ClickOnSpeet(self):
        self.find_element(*self.SPEED_OPTION).click()

    def ClickOnMenuOption(self, option):
        time.sleep(2)
        self.scrollUp()
        self.MENU_OPTION = (By.XPATH, f"(//android.widget.TextView[@text='{option}'])")
        findlement  = True
        while findlement:
            try:
                self.find_element(*self.MENU_OPTION).click()
                findlement = False
            except:
                self.scrollDown()





