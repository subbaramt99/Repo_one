import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
class driverOptions:
    driver_options = webdriver.EdgeOptions()
    driver_options.add_argument("--start-maximized")  # Browser will start with maximized screen
    driver_options.add_argument("headless")  # Browser will invoke without head
    driver_options.add_argument("--ignor-certificate-errors")  # It will ignore all browser certification errors
    # Need to pass all the options to driver
    driver = webdriver.Edge(options=driver_options)  # Need to pass all the options to driver
    # driver = webdriver.Chrome()
    # driver = webdriver.Chrome(executable_path = "C:\SUBBARAM T\Applications\selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    url = "http://rahulshettyacademy.com"
    driver.get("https://rahulshettyacademy.com/seleniumPractise")
    print(driver.title)
    # driver.get(url)
    time.sleep(3)
