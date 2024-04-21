from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By


@pytest.mark.navigateusingid
def test_navigate_by_id():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    element = driver.find_element(By.ID,"btn-make-appointment")
    time.sleep(5)
    element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(10)
    driver.quit()
