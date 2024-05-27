import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
#driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(4)
#driver.find_element(By.ID, "tinymce").clear() # Unable to loacte the element

driver.switch_to.frame("mce_0_ifr")  # The control will move into frames, while switiching to frame need to pass frame ID
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Hi Nivetha How are you")
time.sleep(5)
driver.switch_to.default_content() #The control will move to default page

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(4)
driver.switch_to.frame("courses-iframe") # while switiching to frame need to pass frame ID
#driver.find_element(By.XPATH, "//div/a[@class = 'theme-btn register-btn']").click()
driver.find_element(By.XPATH, "//li/a[@class = 'new-navbar-highlighter']").click()   #//li/a[contains(text(),'Mentorship')]
time.sleep(3)
#driver.switch_to.default_content()
#driver.find_element(By.XPATH, "//input[@id= 'checkBoxOption1']").click()
#driver.find_element(By.XPATH, "//input[@id= 'checkBoxOption2']").click()
#driver.find_element(By.XPATH, "//input[@id= 'checkBoxOption3']").click()
#time.sleep(3)