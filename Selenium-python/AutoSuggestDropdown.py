import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

Practise_url = "https://rahulshettyacademy.com/dropdownsPractise/"

driver.get(Practise_url)
#driver.maximize_window()
#driver.implicitly_wait(500000)
driver.find_element(By.ID, "autosuggest").send_keys("IND")
time.sleep(2)
# Auto suggested dropdown
countries = driver.find_elements(By.CSS_SELECTOR, "li[class = ui-menu-item] a")
print(len(countries))
#print(str(countries))
for country in countries:
    #print(country.text)
    if country.text == "India":
        country.click()
        break
#    print(country.text)
#print(driver.find_element(By.ID, "autosuggest").text)

# Printing the value which is entered in autosuggested dropdown using get.attribute 'value'
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

assert (driver.find_element(By.ID, "autosuggest").get_attribute("value")) == "India"
print("Entered India successfully")


