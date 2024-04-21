from selenium import webdriver
import pytest
import time

@pytest.mark.smoke
def test_open_login_page_url():
    driver = webdriver.Chrome()  # This means open the browser  and Create a session with the POST requests.
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(5)
    driver.quit()
    #Close all the window and tabs.
    #Session id == null(invalid)
    time.sleep(5)

