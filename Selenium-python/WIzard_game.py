import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()

driver.get("https://www.saucedemo.com/")
#driver.implicitly_wait(5000)
driver.find_element(By.XPATH, "//input[@id = 'user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@id = 'login-button']").click()
#url = driver.current_url()
#print(url)
Logo = driver.find_element(By.XPATH, "//div[@class = 'app_logo']").is_displayed()
assert Logo == True
print(Logo)
#print(driver.title)
#print(driver.current_url)
#driver.implicitly_wait(5000)


#driver.get("https://www.saucedemo.com/")
#driver.implicitly_wait(5000)
#driver.find_element(By.XPATH, "//input[@id = 'user-name']").send_keys("locked_out_user")
#driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("secret_sauce")
#driver.find_element(By.XPATH, "//input[@id = 'login-button']").click()
#print("user logged in successfully")
#driver.implicitly_wait(5000)
#ErMsg = driver.find_element(By.XPATH, "//button[@class = 'error-button']").text
#print(ErMsg)
#assert "Sorry, this user has been locked out." in ErMsg
#driver.implicitly_wait(5000)


static_dropdown = Select(driver.find_element(By.XPATH, "//select[@class = 'product_sort_container']"))
static_dropdown.select_by_index(2)
time.sleep(2)
print("user sorted the products from low price to high price")

prices = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_price'][1]")
cost = []
for price in prices:
    cost.append(price.text)
print(cost)
#print(min(cost))
#print(prices)

driver.find_element(By.XPATH, "//button[@class = 'btn btn_primary btn_small btn_inventory ']").click()
print("user added minimum value product")
#time.sleep(1)

driver.find_element(By.XPATH, "//div/a[@class = 'shopping_cart_link']").click()
#time.sleep(1)

driver.find_element(By.XPATH, "//button[@class = 'btn btn_action btn_medium checkout_button ']").click()
#time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder = 'First Name']").send_keys("Jhon")
#time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder = 'Last Name']").send_keys("Doe")
driver.find_element(By.XPATH, "//input[@placeholder = 'Zip/Postal Code']").send_keys("123")
#time.sleep(2)
driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
#time.sleep(2)
print("order submitted")
total = driver.find_element(By.XPATH, "//div[@class = 'summary_total_label']").text
print(total)
assert "8.63" in total
driver.find_element(By.XPATH, "//button[@id = 'finish']").click()
complete_order = driver.find_element(By.XPATH, "//div/h2[@class = 'complete-header']").text
print(complete_order)
assert "Thank you for your order!" == complete_order
time.sleep(2)