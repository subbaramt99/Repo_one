import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()

Edge_Option = webdriver.EdgeOptions
#Edge_Option.add_argument("headless") # Browser will run without head (Browser action will not happen in UI)
#Edge_Option.add_argument("--ignor-certification-errors")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
driver.execute_script("window.scroll(0,600);") # It will execute javascript
# we can get this javascript in browser console
driver.get_screenshot_as_file("screen.png") # It will take screen shot and save as screen.jpeg
driver.execute_script("window.scroll(0,document.body.scrollHeight);") # It will go to end of the page
driver.get_screenshot_as_png() # It will take screen shot and as screen.png
time.sleep(2)