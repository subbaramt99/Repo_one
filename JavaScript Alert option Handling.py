import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
name = "XYZ"
#driver.find_element(By.XPATH, "//input[@id = 'name']").send_keys("XYZ")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.XPATH, "//input[@id = 'alertbtn']").click()
time.sleep(2)
driverAlrt = driver.switch_to.alert
alertText = driverAlrt.text
print(alertText)
time.sleep(2)
driverAlrt.accept()
#driverAlrt.dismiss()
assert name in alertText

time.sleep(3)