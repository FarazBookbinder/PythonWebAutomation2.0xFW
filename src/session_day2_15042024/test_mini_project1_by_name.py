from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By


# <input type="text" name="username" id="username">
# <input type="password" name="password" id="password">
# <button id="submit" class="btn">Submit</button>


def test_navigate_by_name():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    time.sleep(5)
    username_element = driver.find_element(By.NAME, "username")
    username_element.send_keys("student")
    time.sleep(10)
    password_element = driver.find_element(By.NAME, "password")
    password_element.send_keys("Password123")
    time.sleep(15)
    login_element = driver.find_element(By.ID, "submit")
    login_element.click()
    time.sleep()
    assert driver.current_url == "https://practicetestautomation.com/logged-in-successfully/"
    driver.quit()
