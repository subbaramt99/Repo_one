import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkBoxes = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
print(len(checkBoxes))
for checkbox in checkBoxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        # print(checkbox.is_selected())
        time.sleep(2)
        break

assert driver.find_element(By.ID, "displayed-text")
