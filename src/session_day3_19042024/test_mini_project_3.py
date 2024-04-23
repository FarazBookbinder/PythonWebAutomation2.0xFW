import selenium
import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@pytest.mark.smokeverification
def test_verify_error_message():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()
    time.sleep(5)
    username_field = driver.find_element(By.XPATH,"//input[@id='username']")
    username_field.send_keys("augtest_040823@idrive.com")
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot1", attachment_type=AttachmentType.PNG)
    time.sleep(3)
    password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    password_field.send_keys("123456")
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot2", attachment_type=AttachmentType.PNG)
    time.sleep(5)
    click_event = driver.find_element(By.XPATH,"//button[@id='frm-btn']")
    click_event.click()
    time.sleep(25)
    driver.quit()
