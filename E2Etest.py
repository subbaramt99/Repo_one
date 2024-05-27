import time

from selenium import webdriver
from selenium.webdriver.common.service import Service
service_obj = Service("C:\SUBBARAM T\Applications\selenium\chromedriver-win64")
driver = webdriver.Chrome(options= service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(2)