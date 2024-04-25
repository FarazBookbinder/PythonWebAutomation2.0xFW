import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

def test_verify_validation_error():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.maximize_window()
    time.sleep(15)
    driver.switch_to.frame(driver.find_element(By.ID, "result"))
    driver.find_element(By.ID,"email").send_keys("montubinder3@gmail.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "password2").send_keys("123456")
    driver.find_element(By.TAG_NAME,"button").click()
    time.sleep(5)
    validation_error = driver.find_element(By.XPATH, "//small[normalize-space()='Username must be at least 3 characters']").text
    assert validation_error == "Username must be at least 3 characters"
    allure.attach(driver.get_screenshot_as_png(), name="Mini Project3", attachment_type=AttachmentType.PNG)
    driver.quit()



























# //small[text()='Username must be at least 3 characters']/ancestor::div





