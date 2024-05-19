from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_shadow_dom_js():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()

    # Find the element containing the shadow DOM
    page = driver.find_element(By.XPATH, "//div[@class='jackPart']")

    # Scroll into view
    driver.execute_script("arguments[0].scrollIntoView(true);", page)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.jackPart")))

    # Access the shadow DOM elements using JavaScript
    pizza_input = driver.execute_script("""
                return document.querySelector('div.jackPart')
                .shadowRoot.querySelector('div#app2')
                .shadowRoot.querySelector('input#pizza');""")
    # Interact with the shadow DOM element
    pizza_input.send_keys('FarmHouse')
    time.sleep(3)

    driver.quit()