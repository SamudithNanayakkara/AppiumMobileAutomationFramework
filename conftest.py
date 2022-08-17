import pytest
from appium import webdriver

@pytest.fixture(scope="class")
def setup(request):

    desired_caps = {
        "deviceName": "R58R31LQRER",
        "platformName": "Android",
        "appPackage": "my.com.klk.operations",
        "appActivity": "crc64c3e2c0abb9ff2cdd.SplashActivity",
        "noReset": True
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    print("Appium connection started")
    request.cls.driver=driver

    yield
    driver.quit()
