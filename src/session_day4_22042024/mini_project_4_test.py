import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


def test_project_search():
    driver: WebDriver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    driver.find_element(By.ID, "gh-ac").send_keys("16gb")
    driver.find_element(By.XPATH, "//input[@id='gh-btn']").click()

    list_of_product_name = driver.find_elements(By.XPATH, "//span[@role='heading']")
    for idx, product_title in enumerate(list_of_product_name[1:61]):
            product_name = product_title.text
            print(idx, "-", product_name)

    list_of_product_price = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")
    print(type(list_of_product_price))

    product_price_data = []
    for idx, product_price in enumerate(list_of_product_price[1:61]):
        price = product_price.text
        print(idx, "-", price)

        if "to" in price:
            value_is = price.split("to")[0].replace("$", "").strip()
            print("Split price is : ", value_is)

            price_float = float(value_is)  # convert the price from "str" to "float"
            product_price_data.append(price_float)

        else:  # get the price when item having single price
            value_is = price.replace("$", "").strip()
            price_float = float(value_is)  # convert the price from "str" to "float"
            product_price_data.append(price_float)  # Add every item price in prize list at the end

        lowest_prize = min(product_price_data)  # get the lowest price from the price list
        print("Lowest price is : ", lowest_prize)  # print the lowest price