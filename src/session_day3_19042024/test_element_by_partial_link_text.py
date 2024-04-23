from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import allure

# <a id="btn-make-appointment" href="./profile.php#login" class="btn btn-dark btn-lg">Make Appointment</a>


def test_navigate_by_link_text():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    make_apt_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Appointment")
    time.sleep(15)
    make_apt_btn.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(15)
    print(driver.current_url)
    driver.quit()
