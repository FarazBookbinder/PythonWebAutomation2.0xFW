from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_xpath_function_using_contains():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    try:
        appointment_button = (WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Make Appoint')]"))))
        appointment_button.click()
    finally:
        driver.quit()