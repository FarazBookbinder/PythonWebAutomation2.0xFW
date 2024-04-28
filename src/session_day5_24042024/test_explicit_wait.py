from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_explicit_wait():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    driver.find_element(By.XPATH, "//input[@id='login-username']").send_keys("admin@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='login-password']").send_keys("admin")
    driver.find_element(By.XPATH, "//span[@data-qa='ezazsuguuy']").click()
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))
    )
    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    # driver.find_element(By.ID,"js-notification-box-msg")
    driver.quit()
