from selenium import webdriver
from selenium.webdriver.common.by import By

def test_check_implicit_wait():
    driver = webdriver.Chrome()
    # driver.implicitly_wait(5)
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//input[@id='login-username']").send_keys("admin@gmail.com")
    driver.find_element(By.XPATH,"//input[@id='login-password']").send_keys("admin")
    driver.quit()
