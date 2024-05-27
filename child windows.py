import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.implicitly_wait(4)
driver.get("https://the-internet.herokuapp.com/windows")

#driver.find_element(By.CLASS_NAME, "current").click()
driver.find_element(By.XPATH, "//a[@href = '/windows/new']").click()

windowsopened = driver.window_handles  # it will store all the windows which are open in browser as list in indexes
driver.switch_to.window(windowsopened[1])  # The control will move to 1st window


print(driver.title)
assert "New Window" == driver.find_element(By.TAG_NAME, "h3").text

driver.switch_to.window(windowsopened[0])
print(driver.title)
assert "The Internet" == driver.title





