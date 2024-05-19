import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_find_locator_using_relativelocator():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    yoe_radio_button = driver.find_element(locate_with(By.ID, "exp-2").to_right_of(
        {By.XPATH: "//div[@class='control-group']//span[text()='Years of Experience']"}))
    yoe_radio_button.click()
    time.sleep(7)
    driver.quit()
