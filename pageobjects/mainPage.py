from selenium.webdriver.common.by import By

from pageobjects.mainMenu import mainMenu

class mainPage(mainMenu):
    FROM_ = (By.XPATH,"(//android.widget.ImageView[@content-desc='Drop down'])[1]")
    TO_ = (By.XPATH, "(//android.widget.ImageView[@content-desc='Drop down'])[2]")

    FROM_VALUE = (By.ID,"com.ba.universalconverter:id/source_value_placeholder")
    TO_VALUE = (By.ID,"com.ba.universalconverter:id/target_value_placeholder")

    UNIT_OPTION = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.TextView[1]")

    def ClickOnFrom(self):
        self.find_element(*self.FROM_).click()

    def ClickOnTo(self):
        self.find_element(*self.TO_).click()

    def selectUnit(self):
        self.find_element(*self.UNIT_OPTION).click()

    def get_valueFrom(self):
        return self.find_element(*self.FROM_VALUE).get_attribute("text")

    def get_valueTo(self):
        return self.find_element(*self.TO_VALUE).get_attribute("text").replace(" ","")

