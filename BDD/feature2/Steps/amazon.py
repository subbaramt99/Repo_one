import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class naga:
    driver = webdriver.Edge()
    #driver.implicitly_wait(3)
    @given ('Login to amazon')
    def Login_amazon(context):
        context.driver = webdriver.Edge()
        context.driver.get("https://www.amazon.com/")
        time.sleep(2)
        context.driver.implicitly_wait(3)
    #@when ('Entering user name and password')

