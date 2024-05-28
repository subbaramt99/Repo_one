import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
action = ActionChains(driver)
#action.click_and_hold()
#action.context_click()     #Right click
#action.drag_and_drop()     #Drag and drop

action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()    #Hover the button
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
#action.context_click(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
time.sleep(5)
action.double_click(driver.find_element(By.ID, "checkBoxOption1")).perform()
time.sleep(5)
