from selenium import webdriver
import pytest
import time


@pytest.mark.navigateprogram
def test_navigate_urls():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    driver.maximize_window()
    time.sleep(20)  # Using sleep command not to sleep webdriver it's Interpreter stop the execute program.
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    print(driver.title)

#so with the python only below commands are present.
# driver.back
# drover.forward
# driver.refresh