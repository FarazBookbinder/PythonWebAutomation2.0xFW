from selenium import webdriver
import pytest
import time

@pytest.mark.smoke
def test_open_login_page_url():
    driver = webdriver.Chrome()  # This means open the browser  and Create a session with the POST requests.
    driver.get("https://practicetestautomation.com/practice-test-login/")
    print(driver.title)
    driver.maximize_window()
    #print(driver.page_source)
    print(driver.session_id)
    assert driver.title == "Test Login | Practice Test Automation"
    time.sleep(5)
    # using get request means ask to drivers api communication with the browser deriver to open a link.
    # Get request to url parameter.
