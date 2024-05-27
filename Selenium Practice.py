from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

# service = Service(executable_path="C:\edgedriver_win64\msedgedriver.exe")
# options = webdriver.EdgeOptions()
# driver = webdriver.Edge(service=service, options=options)

driver = webdriver.Edge()

#driver = webdriver.Edge(executable_path="C:\SUBBARAM T\Applications\selenium\chromedriver-win64\edgedriver_win64\msedgedriver.exe")

driver.get("https://rahulshettyacademy.com/")
driver.find_element(By.XPATH, "(//li/a[text()='Practice'])[1]").click()
driver.implicitly_wait(5000)
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("SUBBARAM")
driver.implicitly_wait(5000)
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("subbaramt19121999@gmail.com")
driver.implicitly_wait(5000)
driver.find_element(By.XPATH, "//input[@id='agreeTerms']").click()
driver.implicitly_wait(5000)
driver.find_element(By.XPATH, "//button[@id='form-submit']").click()
driver.implicitly_wait(5000)

driver.find_element(By.XPATH, "//div/a[text()='Automation Practise - 2']").click()
driver.implicitly_wait(5000)

# Static dropdown
# Practise url = https://rahulshettyacademy.com/AutomationPractice/
static_dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
static_dropdown.select_by_index(2)
driver.implicitly_wait(5000)
static_dropdown.select_by_value("option3")
driver.implicitly_wait(5000)

# Practise url = https://rahulshettyacademy.com/dropdownsPractise/


driver.minimize_window()

print(driver.current_url)