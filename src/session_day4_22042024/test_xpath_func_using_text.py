import selenium
import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_xpath_function_using_text():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    try:
        # Wait for the 'Make Appointment' button to be clickable
        # WebDriverWait: This sets up an explicit wait with a timeout of 10 seconds, ensuring that Selenium will wait for up to 10 seconds for the element to become clickable before raising a TimeoutException.
        appointment_button = (WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Make Appointment']"))))
            # EC.element_to_be_clickable: This is an Expected Condition that checks if the element is present in the DOM and is clickable.
        appointment_button.click()
    finally:
        driver.quit()
test_xpath_function_using_text()
