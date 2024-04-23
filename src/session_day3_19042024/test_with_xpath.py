import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType


# <a id="btn-make-appointment" href="./profile.php#login" class="btn btn-dark btn-lg">Make Appointment</a>
@pytest.mark.smoke
@allure.title("This is the Mini project")
def test_navigate_by_xpath():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot2", attachment_type=AttachmentType.PNG)
    appointment_btn = driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
    appointment_btn.click()
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot1", attachment_type=AttachmentType.PNG)
    time.sleep(5)
    print(driver.current_url)
    driver.quit()
