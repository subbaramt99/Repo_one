import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Edge()
action = ActionChains(driver)
driver.get("https://www.cvfshp.openreach.co.uk/SHP/#/login")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@placeholder = '    User Id']")
# action.click(on_element=element1).perform()
# action.send_keys("cpbtgs").perform()
print("click1")
driver.find_element(By.XPATH, "//input[@placeholder = '    Password']")
print("click2")
# action.click(on_element=element2).perform()
# action.send_keys("cpbtgs").perform()

time.sleep(4)
driver.find_element(By.CLASS_NAME, "btn")
# action.click(on_element=element3).perform()
print("clicked login")
time.sleep(25)
