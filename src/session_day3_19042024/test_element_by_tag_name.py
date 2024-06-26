import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType


# <a id="btn-make-appointment" href="./profile.php#login" class="btn btn-dark btn-lg">Make Appointment</a>
@pytest.mark.smoke
@allure.title("This is the Mini project")
def test_navigate_by_link_text():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot2", attachment_type=AttachmentType.PNG)
    list_appt_btn = driver.find_elements(By.TAG_NAME, "a")
    make_apt_btn = list_appt_btn[5]
    make_apt_btn.click()
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot1", attachment_type=AttachmentType.PNG)
    time.sleep(15)
    print(driver.current_url)
    driver.quit()
