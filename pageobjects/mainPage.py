from selenium.webdriver.common.by import By

from pageobjects.mainMenu import mainMenu

class mainPage(mainMenu):
    FROM_ = (By.XPATH,"(//android.widget.ImageView[@content-desc='Drop down'])[1]")
    TO_ = (By.XPATH, "(//android.widget.ImageView[@content-desc='Drop down'])[2]")

    FROM_VALUE = (By.ID,"com.ba.universalconverter:id/source_value")
    TO_VALUE = (By.ID,"com.ba.universalconverter:id/target_value")

    #UNIT_OPTION = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.TextView[@text='cm']")

    def ClickOnFrom(self):
        self.find_element(*self.FROM_).click()

    def ClickOnClear(self,val):
        self.NUMBER_BUTTON = (By.XPATH, f"//android.widget.Button[contains(@text, '{val}')]")
        self.find_element(*self.NUMBER_BUTTON).click()

    def ClickOnNumber(self, num):
        for n in str(num):
            self.NUMBER_BUTTON = (By.XPATH, f"//android.widget.Button[contains(@text, '{n}')]")
            self.find_element(*self.NUMBER_BUTTON).click()

    def ClickOnTo(self):
        self.find_element(*self.TO_).click()

    def selectUnit(self, unit):
        self.scrollUp()
        self.UNIT_OPTION = (By.XPATH, f"//android.widget.TextView[contains(@text, '{unit}')]")
        while (not(self.find_element(*self.UNIT_OPTION).is_displayed())):
            self.scrollDown()
        self.find_element(*self.UNIT_OPTION).click()

    def get_valueFrom(self):
        return self.find_element(*self.FROM_VALUE).get_attribute("text")

    def get_valueTo(self):
        return self.find_element(*self.TO_VALUE).get_attribute("text").replace(" ","")

