import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_js_alerts_accept():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    time.sleep(5)
    button = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Faraz")
    alert.accept()
    results = driver.find_element(By.XPATH, " //p[@id='result']")
    print(results.text)
    assert "Faraz" in results.text
    driver.quit()


def test_js_alerts_dismiss():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    time.sleep(5)
    button = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Faraz")
    alert.dismiss()
    driver.quit()
