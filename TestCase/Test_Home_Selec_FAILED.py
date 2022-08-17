import pytest
from pytest_html_reporter import attach
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Test_Home_Selec_FAILED():

    def test_Home_OC(self):
        print("------Execution started: Home Selection------")

        self.driver.implicitly_wait(10)

        # 1. Is 'OK' visible?
        ok = self.driver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc = 'OK']")
        assert ok.is_displayed()
        print("1. OK button is visible")

        # 2. Click 'OK'
        ok.click()
        print("2. OK button is clicked")

        # 3. Does 'Home1' contain 'Home'?
        home1 = self.driver.find_element(By.XPATH,
                                         "//android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[@text = 'Home']")
        step_output = home1.text
        attach(data=self.driver.get_screenshot_as_png())
        assert step_output and ("Homeee" in step_output)
        print("3. 'Home' is visible")

        # 4. Does 'Registration' contain 'Registration'?
        registration = self.driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Registration']")
        step_output = registration.text
        assert step_output and ("Registration" in step_output)
        print("4. 'Registration' text is visible")

        # 5. Does 'Sync' contain 'Sync'?
        sync = self.driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Sync']")
        step_output = sync.text
        assert step_output and ("Sync" in step_output)
        print("5. 'Sync' text is visible")

        # 6. Does 'NFC' contain 'NFC'?
        nfc = self.driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'NFC']")
        step_output = nfc.text
        assert step_output and ("NFC" in step_output)
        print("6. 'NFC' text is visible")

        # 7. Does 'Logout' contain 'Logout'?
        logout = self.driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Logout']")
        step_output = logout.text
        assert step_output and ("Logout" in step_output)
        print("7. 'Logout' text is visible")

        # 8. Click 'Home1'
        home1.click()
        print("8. 'Home' is clicked")

        # 9. Click 'ANDROID.WIDGET.IMAGEBUTTON'
        android_widget_imagebutton = self.driver.find_element(By.XPATH,
                                                              "//android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageButton")
        android_widget_imagebutton.click()
        print("9. 'Change OC' button is clicked")

        # 10. Does 'Operating Centre' contain 'Operating Centre'?
        operating_centre = self.driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Operating Centre']")
        step_output = operating_centre.text
        assert step_output and ("Operating Centre" in step_output)
        print("10. 'Operating Centre' text is visible")

        # 11. Does 'LADANG LEKIR1' contain 'LADANG LEKIR'?
        ladang_lekir1 = self.driver.find_element(By.XPATH,
                                                 "//android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[@text = 'LADANG LEKIR']")
        step_output = ladang_lekir1.text
        assert step_output and ("LADANG LEKIR" in step_output)
        print("11. 'LADANG LEKIR' text is visible")

        # 12. Click 'OKAY'
        okay = self.driver.find_element(By.XPATH, "//android.widget.Button[@text = 'OKAY']")
        okay.click()
        print("12. 'OKAY' is clicked")

        print("------Execution Finished: Home Selection------")

