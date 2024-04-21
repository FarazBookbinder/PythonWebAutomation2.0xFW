from selenium import webdriver
import time


def test_open_browser():
    driver = webdriver.Chrome() # Create a session with the POST requests.
    time.sleep(5)
