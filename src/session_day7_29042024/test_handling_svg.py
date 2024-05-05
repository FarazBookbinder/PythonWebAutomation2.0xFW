import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_handling_svg_for_map():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()
    time.sleep(5)
    list_of_states = driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    for state in list_of_states:
        print(state.get_attribute("aria-label"))
        if "Gujarat" in state.get_attribute("aria-label"):
            state.click()
            break
    time.sleep(10)
    driver.quit()
