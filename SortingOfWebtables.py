import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#driver.find_element(By.XPATH, "//th[@aria-label = 'Veg/fruit name: activate to sort column ascending']").click()
driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()
# If the above browser sort is not happen then assert will fail
driver.get_screenshot_as_file("tablet sort.png")
# get all the list of table items
# Xpath we can wirte in console as well Ex: $x(//tr/td[1])

itemsWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
# The above list contains web elements only it not a text or value of the elements.
products = [] # creating a list of product
for item in itemsWebElements:
    #item.find_element(By.XPATH, "//tr/td[1]").get_attribute("value")
    products.append(item.text)  # Adding the text of webelement into product list
browserSortedList = products.copy()  #copy method can create another copy of the list
print(browserSortedList)
products.sort()
print(products)

assert products == browserSortedList
print("Browser sort is correct")
