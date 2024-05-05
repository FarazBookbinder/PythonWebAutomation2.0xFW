import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_action_first():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    actions = ActionChains(driver=driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name, "F").key_up(Keys.SHIFT).send_keys_to_element(first_name, "araz").perform()

    time.sleep(9)
    driver.quit()
