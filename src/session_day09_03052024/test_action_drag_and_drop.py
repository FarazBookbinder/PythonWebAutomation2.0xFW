import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_action_class_drag_n_drop():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    action = ActionChains(driver)
    from_element = driver.find_element(By.XPATH, "//div[@id='column-a']")
    to_element = driver.find_element(By.XPATH, "//div[@id='column-b']")
    action.click_and_hold(from_element).move_to_element(to_element).release(to_element).perform()
    time.sleep(5)
    driver.quit()
