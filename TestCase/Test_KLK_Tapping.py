from time import sleep
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Test_KLK_Tapping():

    def test_Tapping(self):

        print("Test case execution started")

        self.driver.implicitly_wait(9)

        # 1. Does 'LADANG LEKIR' contain 'LADANG LEKIR'?
        ladang_lekir = self.driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'LADANG LEKIR']")
        step_output = ladang_lekir.text
        assert step_output and ("LADANG LEKIR" in step_output)

        # 2. Does 'Tapping' contain 'Tapping'?
        tapping = self.driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Tapping']")
        step_output = tapping.text
        assert step_output and ("Tapping" in step_output)

        # 3. Click 'Tapping'
        tapping.click()

        self.driver.implicitly_wait(4)

        # 4. Does 'Bucket/Cage Weighing' contain 'Bucket/Cage Weighing'?
        bucket_slash_cage_weighing = self.driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Bucket/Cage Weighing']")
        step_output = bucket_slash_cage_weighing.text
        assert step_output and ("Bucket/Cage Weighing" in step_output)

        # 5. Click 'Bucket/Cage Weighing'
        bucket_slash_cage_weighing = self.driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Bucket/Cage Weighing']")
        bucket_slash_cage_weighing.click()

        self.driver.implicitly_wait(4)

        # 6. Does 'Date' contain 'Date'?
        date = self.driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Date']")
        step_output = date.text
        assert step_output and ("Date" in step_output)

        # 7. Does 'Weight(kg)' contain 'Weight(kg)'?
        weight_kg_ = self.driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Weight(kg)']")
        step_output = weight_kg_.text
        assert step_output and ("Weight(kg)" in step_output)

        # 8. Click Weight value '0'
        weight_value = self.driver.find_element(By.XPATH, "//android.widget.EditText[@text = '0']")
        weight_value.click()

        # 9. Type '22' in '0'
        weight_value.send_keys("22")

        self.driver.implicitly_wait(3)

        # 10. Is 'SAVE' is clickable/enabled?
        save = self.driver.find_element(By.XPATH, "//android.widget.Button[@text = 'SAVE']")
        assert save.is_enabled()

        # 11. Does 'SAVE' contain 'SAVE'?
        save = self.driver.find_element(By.XPATH, "//android.widget.Button[@text = 'SAVE']")
        step_output = save.text
        assert step_output and ("SAVE" in step_output)

        # 12. Click 'SAVE'
        save.click()

        self.driver.implicitly_wait(4)

        # 13. Does 'Document successfully created' contain 'Document successfully created'?
        document_successfully_created = self.driver.find_element(By.XPATH,"//android.widget.TextView[@text = 'Document successfully created']")
        step_output = document_successfully_created.text
        assert step_output and ("Document successfully created" in step_output)

        # 14. Does 'NEW BUCKET/CAGE WEIGHING' contain 'NEW BUCKET/CAGE WEIGHING'?
        new_bucket_slash_cage_weighing = self.driver.find_element(By.XPATH,"//android.widget.Button[@text = 'NEW BUCKET/CAGE WEIGHING']")
        step_output = new_bucket_slash_cage_weighing.text
        assert step_output and ("NEW BUCKET/CAGE WEIGHING" in step_output)

        # 15. Does 'BACK TO HOME' contain 'BACK TO HOME'?
        back_to_home = self.driver.find_element(By.XPATH, "//android.widget.Button[@text = 'BACK TO HOME']")
        step_output = back_to_home.text
        assert step_output and ("BACK TO HOME" in step_output)

        # 16. Click 'BACK TO HOME'
        back_to_home = self.driver.find_element(By.XPATH, "//android.widget.Button[@text = 'BACK TO HOME']")
        back_to_home.click()

        self.driver.implicitly_wait(3)

        # 17. Does 'Home' contain 'Home'?
        home = self.driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Home']")
        step_output = home.text
        assert step_output and ("Home" in step_output)







